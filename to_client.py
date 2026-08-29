from typing import Literal
from uuid import uuid4

async def progress(target: str, text: str):
    pass

async def request(target: str, data: dict[str, Literal["str", "int", "list", "dict", "float", "bool"]]):
    request_id = str(uuid4())

async def comm(target: str, text: str):
    pass

async def status(target: str, stat: Literal["stopped", "starting", "started"]):
    pass