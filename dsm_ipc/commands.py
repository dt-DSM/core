# imports must go BELOW command declarations!

async def ltls(conn: str, acc: str, message: list):
    """List Top Level Servers"""
    if not check_args(conn, 2, message, [int, int]):
        return
    start, end = message

    TLSs = db.sql.SQL("SELECT tls FROM {schema}.server_types").format(schema=db.SCHEMA)
    result = db.multiple(TLSs)
    return await send_message(conn, "succ", [x[0] for x in result][start:end])

async def srvt(conn: str, acc: str, message: list):
    """Server Types"""
    if not check_args(conn, 3, message, [str, int, int]):
        return
    tls, start, end = message
    
    result = db.get("server_types", (tls,), ("tls",), ("st",))
    return await send_message(conn, "succ", result[start:end])

async def csrv(conn: str, acc: str, message: list):
    """Create Server"""
    if not check_args(conn, 3, message, [str, str, str]):
        return
    tls, st, name = message

    manager = db.get("server_types", (tls,), ("tls",), ("manager",),)
    manager = managers.get(manager)
    if manager is None:
        return await send_message(conn, "cmdf", "Couldn't locate manager")
    
    task = asyncio.create_task(manager.main.create(conn, st, name))
    create_server_tasks.add(task)
    task.add_done_callback(create_server_tasks.discard)

    return await send_message(conn, "succ", "Creating server")

async def rspns(conn: str, acc: str, message: list):
    """Response"""
    pass

async def rsrv(conn: str, acc: str, message: list):
    "Run Server"
    pass

async def ssrv(conn: str, acc: str, message: list):
    "Stop Server"
    pass

async def cfgs(conn: str, acc: str, message: list):
    """Configs"""
    pass

async def scfg(conn: str, acc: str, message: list):
    """Set Config"""
    pass

async def isonl(conn: str, acc: str, message: list):
    """Is Online"""
    pass

async def rcmd(conn: str, acc: str, message: list):
    """Run Command"""
    pass

async def smsg(conn: str, acc: str, message: list):
    """Send Message"""
    pass

# registry creation
cmds = dir()

import sys, asyncio
from collections.abc import Callable
from driftech_lib import db, jsonIO
from globals import managers

create_server_tasks = set()

registry: dict[str, Callable] = {}
module = sys.modules[__name__]
for command in cmds:
    if command.startswith("_"):
        continue
    registry[command] = getattr(module, command)

async def check_args(conn:str, arg_count: int, args: list, types: list[type]):
    if len(args) != arg_count:
        return await send_message(conn, "cmdf", "Incorrect number of arguments")

    for i, v in enumerate(args):
        arg_type = types[i]
        if not isinstance(v, arg_type):
            return await send_message(conn, "cmdf", f"Bad argument {i}")
    
    return True

async def send_message(conn: str, code: str, message):
    msg = f'{code} "{jsonIO.dumps(message)}"'.encode()
    await client_server.send_message(conn, msg) # type: ignore