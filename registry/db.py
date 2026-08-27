import logging, sys
from driftech_lib import db
from globals import data

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
dbd = data["DB"]
db.start(dbd["SCHEMA"], dbd["HOST"], dbd["NAME"], dbd["USER"], dbd["PASS"], dbd["PORT"])

db.table("st", [
    "manager TEXT",
    "tls TEXT PRIMARY KEY",
    "st TEXT"
    ])

db.table("srv", [
    "id BIGSERIAL PRIMARY KEY",
    "name TEXT",
    "owner TEXT"
    ])
