import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask import Blueprint, render_template, request
from threading import Thread, Event
from core.token import CoinbaseExchangeAuth
from services.post_services import PostServices
import setting

bp = Blueprint(__name__, __name__, template_folder='templates')

auth = CoinbaseExchangeAuth(setting.API_KEY, setting.API_SECRET, setting.API_PASS)
post_service = PostServices(auth)

# url
@bp.route('/coinbasepro')
def coinbasepro():
	return render_template('coinbasepro.html')

@bp.route('/coinbasepro/order1', methods = ['POST'])
def order1():
	global post_service
	BTC_GBP_bid = float(request.form['BTC_GBP_bid'])
	ETH_BTC_bid = float(request.form['ETH_BTC_bid'])
	ETH_GBP_ask = float(request.form['ETH_GBP_ask'])

	return post_service.order1(BTC_GBP_bid, ETH_BTC_bid, ETH_GBP_ask)

@bp.route('/coinbasepro/order2', methods = ['POST'])
def order2():
	global post_service
	ETH_GBP_bid = float(request.form['ETH_GBP_bid'])
	ETH_BTC_ask = float(request.form['ETH_BTC_ask'])
	BTC_GBP_ask = float(request.form['BTC_GBP_ask'])

	return post_service.order2(ETH_GBP_bid, ETH_BTC_ask, BTC_GBP_ask)





