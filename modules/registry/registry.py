from ..globals import DIR
from ..utils import jsonIO

st_json = DIR / "registry/server_types.json"

TopLevelServerStr = str
ManagerStr = str
ServerTypeStr = str
server_types: dict[ManagerStr, dict[TopLevelServerStr, list[ServerTypeStr]]] = jsonIO.load(st_json)

def register(manager, new_server_types: dict[str, list]):
    server_types[manager] = new_server_types
    _save()

def remove(manager):
    server_types.pop(manager, None)
    _save()

def _save():
    jsonIO.dump(st_json, server_types)