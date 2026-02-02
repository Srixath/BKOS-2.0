import asyncio
import websockets
import json
import random

async def send_data(websocket):
    try:
        while True:
            # Simulate knee angles
            data = {
                "thigh": {"x": random.uniform(-10, 10), "y": random.uniform(-10, 10), "z": random.uniform(-10, 10)},
                "knee": {"x": random.uniform(-5, 5), "y": random.uniform(-5, 5), "z": random.uniform(-5, 5)},
                "shin": {"x": random.uniform(-10, 10), "y": random.uniform(-10, 10), "z": random.uniform(-10, 10)}
            }
            
            await websocket.send(json.dumps(data))
            await asyncio.sleep(0.5)  # 2 updates per second
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    print("WebSocket server starting on ws://localhost:8765")
    async with websockets.serve(send_data, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())