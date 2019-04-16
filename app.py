from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import lcm
from beanbagbot import command


app = Flask(__name__)
socketio = SocketIO(app)

cmd_msg = command()

@app.route('/')
def main():
    return render_template('index.html')

@socketio.on('cmd')
def user_input(msg):
	# copy the incoming socket message into the LCM message object
	cmd_msg.turn = msg['x']
	cmd_msg.forward = msg['y']
	# and publish the message via LCM
	lc.publish("/beanbagbot/command", cmd_msg.encode())


@socketio.on('activate')
def take_control(msg):
	print('Someone took control')
	socketio.emit('deactivate', {})

if __name__ == '__main__':
	lc = lcm.LCM()
	socketio.run(app, debug=False, port=5000)

