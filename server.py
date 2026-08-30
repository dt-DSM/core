import asyncio, logging, sys
from driftech_lib.ipc import server
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class Server(server.Server):
    async def on_message(self, message):
        return await super().on_message(message)    

if __name__ == "__main__":
    asyncio.run(Server().start("127.0.0.1", 5000))
