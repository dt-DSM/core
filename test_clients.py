import asyncio, logging, sys
from driftech_lib.ipc import client

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

async def main():
    for i in range(10000):
        connection = client.Connector("127.0.0.1", 5000)
        asyncio.create_task(connection.start())
    await asyncio.sleep(60)

asyncio.run(main())
