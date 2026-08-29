import argon2
from driftech_lib import db
ph = argon2.PasswordHasher()

def create(username: str, password: str):
    exists = db.get("account", (username,), ("username",), ("username",))
    if exists:
        return False
    hashed = ph.hash(password)
    db.insert("acc", ("username",), ("password",), (username, hashed))
    return True

def login(username: str, password: str):
    acc = db.get("account", (username,), ("username",), ("password",))
    if acc is None:
        return None
    try:
        ph.verify(acc, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False

def tier(username: str) -> int | None:
    return db.get("account", (username,), ("username",), ("tier",))
