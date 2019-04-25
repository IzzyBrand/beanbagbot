from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        self.broadcast(str(self.address))

    def handleClose(self):
        print(self.address, 'closed')
        clients.remove(self)

    def broadcast(self, message):
        for client in clients:
            print('Broadcasting to: ' + str(client.address))
            client.sendMessage(message)

server = SimpleWebSocketServer('', 5050, SimpleEcho)
server.serveforever()