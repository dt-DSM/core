import asyncio, logging, sys
from driftech_lib.ipc import server
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

if __name__ == "__main__":
    asyncio.run(server.start("127.0.0.1", 5000))
