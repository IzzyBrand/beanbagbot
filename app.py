from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import time

app = Flask(__name__)
socketio = SocketIO(app)

cmd = {'forward': 0, 'turn': 0, 'time': 0}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@socketio.on('cmd')
def user_input(msg):
	cmd.update(msg)
	cmd['time'] = time.time()

@socketio.on('activate')
def take_control(msg):
	print('Someone took control')
	socketio.emit('deactivate', {})


@app.route('/get_cmd', methods=['GET'])
def get_cmd():
	cmd['elapsed'] = time.time() - cmd['time']
	return json.dumps(cmd)

if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', debug=True, port=5000)

