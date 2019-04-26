from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import params as p

clients = []

class ControllerServer(WebSocket):
    # TODO: figure out how to init with super properly to init self.id field

    def handleMessage(self):
        msg = self.data
        try:
            parsed_data = json.loads(msg)
            if 'id' in parsed_data:
                self.id = parsed_data['id']
                print('Received ID: {}'.format(self.id))

            elif 'activate' in parsed_data and self.id is not None:
                data = json.dumps({'id': self.id})
                self.broadcast(data)
                print('{} took control'.format(self.id))

            elif 'forward' in parsed_data:
                print('Received {}\t{}'.format(parsed_data['forward'], parsed_data['turn']))

            else:
                pass

        except:
            print('Failed to parse {}'.format(msg))

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)

    def handleClose(self):
        print(self.address, 'closed')
        clients.remove(self)

    def broadcast(self, message):
        for client in clients:
            print('Broadcasting to: {}'.format(client.id))
            client.sendMessage(message)

server = SimpleWebSocketServer('0.0.0.0', p.websocket_port, ControllerServer)
server.serveforever()