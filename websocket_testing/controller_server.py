from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json

clients = []

class ControllerServer(WebSocket):
    # def __init__(self, server, sock, address):
    #     WebSocket.__init__(self, server, sock, address)
    #     self.id = None

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

            else:
                # this is where we handle receiving control messages
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

server = SimpleWebSocketServer('0.0.0.0', 5050, ControllerServer)
server.serveforever()