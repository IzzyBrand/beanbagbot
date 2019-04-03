from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def main():
    return render_template('index.html')


@socketio.on('cmd')
def request_move(message):
    print('received: ' + str(message))
    # socketio.emit('hi', {}, callback=received)


if __name__ == '__main__':
    socketio.run(app, debug=True)
