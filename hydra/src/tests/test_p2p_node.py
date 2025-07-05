import asyncio
import websockets
import pytest
from src.p2p.node import Wezel


@pytest.mark.asyncio
async def test_wezel():
    wezel = Wezel(8765)
    async def serwer():
        await wezel.start()
    zad = asyncio.create_task(serwer())
    await asyncio.sleep(0.1)
    async with websockets.connect("ws://localhost:8765") as ws1, websockets.connect("ws://localhost:8765") as ws2:
        await ws1.send("hej")
        recv = await ws2.recv()
        assert recv == "hej"
    zad.cancel()
    with pytest.raises(asyncio.CancelledError):
        await zad
