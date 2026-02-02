import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as ws:
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            print("Thigh:", data["thigh"])
            print("Knee: ", data["knee"])
            print("Shin: ", data["shin"])
            print("---")

asyncio.run(test())
