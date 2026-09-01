import argon2
from driftech_lib import db
ph = argon2.PasswordHasher()

logged_in: dict[str, str] = {}

async def create(conn: str, username: str, password: str):
    exists = db.get("account", (username,), ("username",), ("username",))
    if exists:
        return False
    hashed = ph.hash(password)
    db.insert("acc", ("username",), ("password",), (username, hashed))
    logged_in[conn] = username
    return True

async def login(conn: str, username: str, password: str):
    acc = db.get("account", (username,), ("username",), ("password",))
    if acc is None:
        return None
    try:
        ph.verify(acc, password)
        logged_in[conn] = username
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

async def tier(username: str) -> int | None:
    return db.get("account", (username,), ("username",), ("tier",))
