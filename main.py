import time
import numpy as np
import params as p
import asyncio
import websockets
import json

from motors import Motors

cmd = {'forward': 0,
       'turn': 0,
       'time': 0}

async def update_motors():
    global cmd
    m = Motors()
    m.set(0,0)
    while True:
        if time.time() - cmd['time'] > p.motor_command_timeout:
            m.set(0,0)
        else:
            m.set(cmd['forward'], cmd['turn'])

        await asyncio.sleep(0.05)

async def receive_messages():
    global cmd
    socket_addr = 'ws://localhost:{}'.format(p.websocket_port)
    while True:
        try:
            async with websockets.connect(socket_addr) as ws:

                # send our ID to the websocket server
                id_msg = {"id": "motors"}
                await ws.send(json.dumps(id_msg))

                # and then receive messages indefinitely
                async for msg in ws:
                    try:
                        parsed_data = json.loads(msg)
                        if 'forward' in parsed_data and 'turn' in parsed_data:
                            cmd.update(parsed_data)
                            cmd['time'] = time.time()

                    except ValueError:
                        print('Failed to parse {}'.format(msg))

        except OSError:
            print('Failed to connect to {}'.format(socket_addr))
            cmd = (0, 0)
        except websockets.exceptions.ConnectionClosed:
            print('Lost connection to {}'.format(socket_addr))
            cmd = (0, 0)

        await asyncio.sleep(0.5)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(update_motors())
    loop.create_task(receive_messages())
    loop.run_forever()
