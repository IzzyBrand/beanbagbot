import time
import numpy as np
import params as p
import asyncio
import websockets
import json

from motors import Motors

async def run():
    m = Motors()
    m.set(0,0)
    try:
        socket_addr = 'ws://localhost:{}'.format(p.websocket_port)
        async with websockets.connect(socket_addr) as ws:
            # send our ID to the websocket server
            id_msg = {"id": "motors"}
            await ws.send(json.dumps(id_msg))

            # receive messages and set the motors accordingly
            while ws.open:
                try:
                    msg = await ws.recv()
                    parsed_data = json.loads(msg)
                    if 'forward' in parsed_data:
                        m.set(parsed_data['forward'], parsed_data['turn'])

                    # TODO: have a time-out on commands from the motors

                except ValueError:
                    print('Failed to parse {}'.format(msg))

                asyncio.sleep(0.05)

            print('Connection to {} closed'.format(socket_addr))
            m.stop()

    except OSError:
        print('Failed to connect to {}'.format(socket_addr))
        m.stop()
    except websockets.exceptions.ConnectionClosed:
        print('Lost connection to {}'.format(socket_addr))
        m.stop()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(run())
