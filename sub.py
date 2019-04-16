import lcm
from beanbagbot import command
import time

def my_handler(channel, data):
	msg = command.decode(data)
	print("Received {}, {} on {}".format(msg.forward, msg.turn, channel))

lc = lcm.LCM()
subscription = lc.subscribe("/beanbagbot/command", my_handler)

try:
    while True:
        lc.handle()
        
except KeyboardInterrupt:
    pass