from globals import DIR
from driftech_lib import jsonIO

__all__ = ["server_types", "managers"]

st_json = DIR / "registry/server_types.json"
mg_json = DIR / "registry/managers.json"

TopLevelServerStr = str
ManagerStr = str
ServerTypeStr = str
server_types: dict[ManagerStr, dict[TopLevelServerStr, list[ServerTypeStr]]] = jsonIO.load(st_json)
managers: dict[TopLevelServerStr, ManagerStr] = jsonIO.load(mg_json)

def register(manager: ManagerStr, new_server_types: dict[TopLevelServerStr, list[ServerTypeStr]]):
    server_types[manager] = new_server_types
    for nst in new_server_types:
        managers[nst] = manager
    _save()

def remove(manager: ManagerStr):
    server_types.pop(manager, None)
    managers = {k: v for k, v in managers if v != manager}
    _save()

def _save():
    server_types = dict(sorted(server_types.items()))
    jsonIO.dump(st_json, server_types)
    jsonIO.dump(mg_json, managers)