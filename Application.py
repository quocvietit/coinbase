import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging
import setting
from random import random
from time import sleep
from threading import Thread, Event
from utils.logger_initializer import initialize_logger
from core.token import CoinbaseExchangeAuth
from services.get_services import GetServices

from views.coinbasepro import bp as coinbasepro

app = Flask(__name__)

# Register blueprint
app.register_blueprint(coinbasepro)

# turn the flask app into a socketio app
socketio = SocketIO(app)

# random number Generator Thread
thread = Thread()
thread_stop_event = Event()

# init logger
logging.info("Initialize logger")
initialize_logger()

# Get auth
logging.info("Get auth...")
auth = CoinbaseExchangeAuth(setting.API_KEY, setting.API_SECRET, setting.API_PASS)

if auth:
	logging.info("Get auth success!")
else:
	logging.warning("Get auth fail!")

logging.info("Create get services")

# init serive
logging.info("Initialize services")
get_services = GetServices(auth)

class ServiceThread(Thread):
	global get_services

	def __init__(self):
		self.delay = 2
		super(ServiceThread, self).__init__()

	def get_product(self):
		while not thread_stop_event.isSet():
			BTC_GBP = get_services.product("BTC-GBP")
			ETH_GBP = get_services.product("ETH-GBP")
			ETH_BTC = get_services.product("ETH-BTC")

			profit_rate1 = (((1 / ETH_BTC[0]) * ETH_GBP[1]) - BTC_GBP[1]) * (100 / BTC_GBP[0])
			profit_rate2 = ((ETH_BTC[1] * BTC_GBP[1]) - ETH_GBP[0]) * (100 / ETH_GBP[0])

			data = {
				"BTC_GBP_bid": BTC_GBP[0],
				"BTC_GBP_ask": BTC_GBP[1],
				"ETH_GBP_bid": ETH_GBP[0],
				"ETH_GBP_ask": ETH_GBP[1],
				"ETH_BTC_bid": ETH_BTC[0],
				"ETH_BTC_ask": ETH_BTC[1],
				"profit_rate1": profit_rate1,
				"profit_rate2": profit_rate2
			}
			socketio.emit('coinbasepro', data, namespace='/test')
			sleep(self.delay)

	def run(self):
		self.get_product()


@socketio.on('connect', namespace='/test')
def coinbasepro_connect():
	print('Client connect')
	# need visibility of the global thread object
	global thread

	# Start the random number generator thread only if the thread has not been started before.
	if not thread.isAlive():
		thread = ServiceThread()
		thread.start()


@socketio.on('disconnect', namespace='/test')
def coinbasepro_disconnect():
	print('Client disconnected')
	coinbasepro_connect()


if __name__ == '__main__':
	# Create app secret key
	logging.info("Create app secret key")
	secret_key = os.urandom(12)
	app.secret_key = secret_key
	logging.info("APP_SECRET_KEY: " + secret_key.encode("hex"))

	# Run server: localhost:8080
	logging.info("Start server...")
	# socketio.run(app)
	app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
