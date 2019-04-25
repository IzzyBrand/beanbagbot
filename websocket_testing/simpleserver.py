from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []

class BroadcastOnConnect(WebSocket):

    def handleMessage(self):
        print('Received: {}'.format(self.data))

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        self.broadcast(str(self.address))

    def handleClose(self):
        print(self.address, 'closed')
        clients.remove(self)

    def broadcast(self, message):
        for client in clients:
            print('Broadcasting to: {}'.format(client.address))
            client.sendMessage(message)

server = SimpleWebSocketServer('0.0.0.0', 5050, BroadcastOnConnect)
server.serveforever()