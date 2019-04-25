#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import json

async def sender(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(json.dumps({'time': now}))
        await asyncio.sleep(random.random() * 3)

async def receiver(websocket, path):
	while True:
		try:
			msg = await websocket.recv()
			print(msg)
		except websockets.exceptions.ConnectionClosed:
			print(dir(websocket))

# start_server = websockets.serve(sender, '127.0.0.1', 5050)
start_server = websockets.serve(receiver, '127.0.0.1', 5050)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()