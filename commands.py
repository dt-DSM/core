# imports must go BELOW command declarations!

def tls(start: int = None, end: int = None):
    TLSs = db.sql.SQL("SELECT tls FROM {schema}.server_types").format(schema=db.SCHEMA)
    result = db.multiple(TLSs)
    return jsonIO.dumpb([x[0] for x in result][start:end])

def st(tls, start: int = None, end: int = None):
    result = db.get("server_types", (tls,), ("tls",), ("st",))
    return jsonIO.dumpb(result[start:end])

def create(tls: str, st: str, name: str):
    pass

def response(id: str, args: dict):
    pass

def start(server: str):
    pass

def stop(server: str):
    pass

def configs(server: str):
    pass

def set(server: str, config: str, value):
    pass

def status(server: str):
    pass

def cmd(server: str, command: str):
    pass

def msg(server: str, text: str):
    pass

# registry creation
cmds = dir()
import sys
from driftech_lib import jsonIO, db
command_registry = {}
module = sys.modules[__name__]
for command in cmds:
    if command.startswith("_"):
        continue
    command_registry[cmd] = getattr(module, cmd)
