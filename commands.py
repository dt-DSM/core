from registry import registry
from driftech_lib import jsonIO

async def tls(start: int = None, end: int = None):
    return jsonIO.dumpb([k for d in registry.server_types.values() for k in d][start:end])

async def st(tls, start: int = None, end: int = None):
    if manager := registry.managers.get(tls):
        if sts := registry.server_types[manager].get(tls):
            return sts[start:end]
        else:
            return None
    else:
        return None

command_registry = {
    "tls": tls,
    "st": st
}