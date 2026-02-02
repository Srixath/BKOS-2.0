import asyncio
import websockets
import random
import json

async def send_fake_data(websocket, path):
    while True:
        data = {
            "thigh": {"x": random.uniform(-10,10), "y": random.uniform(-10,10), "z": random.uniform(-10,10)},
            "knee":  {"x": random.uniform(-5,5), "y": random.uniform(-5,5), "z": random.uniform(-5,5)},
            "shin":  {"x": random.uniform(-10,10), "y": random.uniform(-10,10), "z": random.uniform(-10,10)}
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(0.5)

async def main():
    async with websockets.serve(send_fake_data, "localhost", 8765):
        print("Fake WebSocket server running on ws://localhost:8765")
        await asyncio.Future()  # run forever

# Run with asyncio.run() to be Windows-compatible
asyncio.run(main())
