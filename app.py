from flask import Flask, render_template
from flask_socketio import SocketIO
import json

app = Flask(__name__)
socketio = SocketIO(app)

cmd = {'x': 0, 'y': 0}

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on('cmd')
def user_input(msg):
	cmd.update(msg)


@socketio.on('activate')
def take_control(msg):
	print('Someone took control')
	socketio.emit('deactivate', {})


@app.route('/get_cmd', methods=['GET'])
def get_cmd():
	return json.dumps(cmd)

if __name__ == '__main__':
	socketio.run(app, debug=True, port=5000)

