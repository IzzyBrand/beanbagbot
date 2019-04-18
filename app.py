from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import time
import params as p

app = Flask(__name__)
socketio = SocketIO(app)

cmd = {'forward': 0, 'turn': 0}
most_recent_command_time = 0

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on('cmd')
def user_input(msg):
	cmd.update(msg)
	most_recent_command_time = time.time()


@socketio.on('activate')
def take_control(msg):
	print('Someone took control')
	socketio.emit('deactivate', {})


@app.route('/get_cmd', methods=['GET'])
def get_cmd():
	if time.time() - most_recent_command_time < p.server_command_timeout:
		return json.dumps(cmd)

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', debug=True, port=5000)

