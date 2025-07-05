from fastapi import FastAPI, WebSocket


def dodaj_ws(app: FastAPI) -> None:
    @app.websocket("/ws")
    async def gniazdo(socket: WebSocket):
        await socket.accept()
        await socket.send_text("Polaczone")
        while True:
            dane = await socket.receive_text()
            await socket.send_text(f"Odebrano: {dane}")
