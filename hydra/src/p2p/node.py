import asyncio
import websockets


class Wezel:
    def __init__(self, port: int) -> None:
        self.port = port
        self.polaczenia: set[websockets.WebSocketServerProtocol] = set()

    async def handler(self, websocket):
        self.polaczenia.add(websocket)
        try:
            async for wiadomosc in websocket:
                for conn in self.polaczenia:
                    if conn is not websocket:
                        await conn.send(wiadomosc)
        finally:
            self.polaczenia.remove(websocket)

    async def start(self):
        async with websockets.serve(self.handler, "0.0.0.0", self.port):
            await asyncio.Future()
