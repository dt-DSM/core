# from registry import registry
from driftech_lib import jsonIO, db

async def tls(start: int = None, end: int = None):
    TLSs = db.sql.SQL("SELECT tls FROM {schema}.server_types").format(schema=db.SCHEMA)
    result = db.multiple(TLSs)
    return jsonIO.dumpb([x[0] for x in result][start:end])

# async def st(tls, start: int = None, end: int = None):
#     if manager := registry.managers.get(tls):
#         if sts := registry.server_types[manager].get(tls):
#             return sts[start:end]
#         else:
#             return None
#     else:
#         return None

command_registry = {
    "tls": tls
}