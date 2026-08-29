# imports must go BELOW command declarations!

async def tls(source: str, start: int = None, end: int = None):
    TLSs = db.sql.SQL("SELECT tls FROM {schema}.server_types").format(schema=db.SCHEMA)
    result = db.multiple(TLSs)
    return [x[0] for x in result][start:end]

async def st(source: str, tls, start: int = None, end: int = None):
    result = db.get("server_types", (tls,), ("tls",), ("st",))
    return result[start:end]

async def create(source: str, tls: str, st: str, name: str):
    manager = db.get("server_types", (tls,), ("tls",), ("manager",),)
    manager = managers.get(manager)
    if manager is None:
        return False
    _ = asyncio.create_task(manager.main.create(source, st, name))
    return True

async def response(source: str, id: str, args: dict):
    pass

async def start(source: str, server: str):
    pass

async def stop(source: str, server: str):
    pass

async def configs(source: str, server: str):
    pass

async def set(source: str, server: str, config: str, value):
    pass

async def status(source: str, server: str):
    pass

async def cmd(source: str, server: str, command: str):
    pass

async def msg(source: str, server: str, text: str):
    pass

# registry creation
cmds = dir()

import sys, asyncio
from driftech_lib import db
from globals import managers

command_registry = {}
module = sys.modules[__name__]
for command in cmds:
    if command.startswith("_"):
        continue
    command_registry[cmd] = getattr(module, cmd)
