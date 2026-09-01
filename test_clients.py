import asyncio
from driftech_lib.ipc import client

async def main():
    connection = client.ConcurrentClient("127.0.0.1", 5000, 5001)
    asyncio.create_task(connection.start())
    await connection.send_message(b"exit")
    await asyncio.sleep(1)

asyncio.run(main())
