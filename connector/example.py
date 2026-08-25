import asyncio
from ..connector.connector import Connector

class Connect(Connector):
    async def on_message(self, message):
        print(message.decode())

async def main():
    connector = Connect()
    asyncio.create_task(connector.start())
    await asyncio.create_task(loop(connector))
    
async def loop(connector: Connect):
    while True:
        await connector.send_message(await asyncio.to_thread(input))
asyncio.run(main())
