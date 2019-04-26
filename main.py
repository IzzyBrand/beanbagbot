import time
import numpy as np
import params as p
import asyncio
import websockets
import json

# from motors import Motors

async def run():
    # m = Motors()
    # m.set(0,0)

    socket_addr = 'ws://localhost:{}'.format(p.websocket_port)
    async with websockets.connect(socket_addr) as websocket:
        data = {"id": "motors"}
        await websocket.send(json.dumps(data))
        while True:
            data = await websocket.recv()
            print(data)
            asyncio.sleep(0.05)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(run())
