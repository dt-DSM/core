from driftech_lib import jsonIO
from driftech_lib.ipc import server
from data import accounts
from dsm_ipc import commands

class ConcurrentServer(server.ConcurrentServer):
    async def on_message(self, conn, message):
        message = message.split(b" ", 1)
        if len(message) == 1:
            return
        command, message = message
        message = jsonIO.loadb(message)
        if command == b"login":
            if len(message) != 2:
                await self.send_message(conn, b"cmdf \"Incorrect number of arguments\"")
                return
            success = await accounts.login(conn, *message)
            if success is None:
                await self.send_message(conn, b"lgnf \"Account not found\"")
                return
            if success is False:
                await self.send_message(conn, b"lgnf \"Incorrect password\"")
                return

        if command == b"nacc":
            if len(message) != 2:
                await self.send_message(conn, b"cmdf \"Incorrect number of arguments\"")
                return
            success = await accounts.create(conn, *message)
            if success is False:
                await self.send_message(conn, b"naccf \"Account already exists\"")
                return

        if acc := accounts.logged_in.get(conn):
            cmd = commands.registry.get(command)
            if not cmd:
                await self.send_message(conn, b"cmdnf \"Command not found\"")
                return
            await cmd(conn, acc, *message)

async def run(HOST: str = "127.0.0.1", PORT: int = 5000):
    client_server = ConcurrentServer(HOST, PORT)
    await client_server.start()
    setattr(commands, "client_server", client_server)
