import asyncio, json
from pathlib import Path
DIR = Path(__file__).resolve().parent
with open(DIR / "data.json", "r") as file:
    data = json.load(file)
HOST = data["HOST"]
PORT = data["PORT"]

async def connector():
    server = await asyncio.start_server(interface, HOST, PORT)
    print(f"[LISTENING] Server is running on {HOST}:{PORT}")
    async with server:
        await server.serve_forever()

async def interface(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"new connection: {addr}")
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            print(f"[{addr}] Received: {data.decode()}")
            writer.write(b"Message processed")
            await writer.drain()  # Ensure data is flushed to the network buffer
    except (asyncio.CancelledError, ConnectionResetError, BrokenPipeError, OSError):
        print(f"[DISCONNECTED] Connection closed for {addr}")
        writer.close()
        await writer.wait_closed()
    finally:
        print(f"[DISCONNECTED] Connection closed for {addr}")
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(connector())