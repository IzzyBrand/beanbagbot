from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
import params as p

clients = []

class ControllerServer(WebSocket):

    def __init__(self, server, sock, address):
        super(ControllerServer, self).__init__(server, sock, address)
        self.id = None

    def handleMessage(self):
        msg = self.data
        try:
            parsed_data = json.loads(msg)
            if 'id' in parsed_data:
                self.id = parsed_data['id']
                print('Received ID: {}'.format(self.id))

            elif 'activate' in parsed_data and self.id is not None:
                message = json.dumps({'id': self.id})
                self.broadcast(message)
                print('{} took control'.format(self.id))

            elif 'forward' in parsed_data:
                print('Received {}\t{}'.format(parsed_data['forward'], parsed_data['turn']))

                for client in clients:
                    if client.id == 'motors':
                        client.sendMessage(msg)

            else:
                pass

        except ValueError:
            print('Failed to parse {}'.format(msg))

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)

    def handleClose(self):
        print(self.address, 'closed')
        clients.remove(self)

    def broadcast(self, message):
        [c.sendMessage(message) for c in clients if c.id != 'motors']

server = SimpleWebSocketServer('0.0.0.0', p.websocket_port, ControllerServer)
server.serveforever()