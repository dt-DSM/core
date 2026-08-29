import logging, sys
from driftech_lib import db
from globals import data

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
dbd = data["DB"]
db.start(dbd["SCHEMA"], dbd["HOST"], dbd["NAME"], dbd["USER"], dbd["PASS"], dbd["PORT"])

def register_manager(manager: str, TLSs: dict[str, list[str]]):
    for tls, STs in TLSs:
        for st in STs:
            db.insert("server_types", ("tls",), ("manager", "st"), (manager, tls, st))

def remove_manager(manager):
    db.delete("server_types", ("manager",), (manager,),)

db.table("server_types", [
    "manager TEXT",
    "tls TEXT PRIMARY KEY",
    "st TEXT[]"
    ])

db.table("servers", [
    "id BIGSERIAL PRIMARY KEY",
    "name TEXT",
    "owner TEXT"
    ])

db.table("accounts", [
    "username TEXT PRIMARY KEY",
    "password TEXT",
    "tier BIGINT DEFAULT 0"
    ])

db.insert("server_types", ("tls",), ("manager", "st"), ("minecraft", "minecraft", ["forge", "fabric"]))
db.insert("server_types", ("tls",), ("manager", "st"), ("factorio", "factorio", ["factorio"]))