from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('index.html')


def received(msg):
    print(msg)


@socketio.on('emit')
def request_move(message):
    print('hi')
    socketio.emit('hi', {}, callback=received)


if __name__ == '__main__':
    socketio.run(app)
