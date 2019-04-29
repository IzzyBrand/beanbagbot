from flask import Flask, render_template
import json
import time
import params as p

app = Flask(__name__)

cmd = {'forward': 0, 'turn': 0, 'time': 0}

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=p.flask_port)

