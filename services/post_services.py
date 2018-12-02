import sys

reload(sys)
sys.setdefaultencoding('utf8')

import setting
import requests


class PostServices:
	def __init__(self, auth):
		self.__auth = auth
		self.__url = setting.URL_ORDER

	def order(self, params1, params2, params3):
		try:
			req1 = requests.post(self.__url, json=params1, auth=self.__auth)
			req2 = requests.post(self.__url, json=params2, auth=self.__auth)
			req3 = requests.post(self.__url, json=params3, auth=self.__auth)

			req1 = req1.json()
			req2 = req2.json()
			req3 = req3.json()

			return self.format_results(req1, req2, req3)
		except:
			return "Error!"

	def format_results(self, req1, req2, req3):
		res1 = self.format_result(1, req1)
		res2 = self.format_result(2, req2)
		res3 = self.format_result(3, req3)

		return "{}<br/>{}<br/>{}".format(res1, res2, res3)

	def format_result(self, step, req):
		txt_format = "Step{}: <br/>Product: {} - Price: {}  <br/> Size: {}  -  Side: {}<br/>"
		return txt_format.format(step, req["product_id"], req["price"], req["size"], req["side"])

	def order1(self, BTC_GBP_bid, ETH_BTC_bid, ETH_GBP_ask):
		BTC_GBP_size = 0.002
		BTC_GBP_params = {
			"size": BTC_GBP_size,
			"price": BTC_GBP_bid,
			"side": "buy",
			"product_id": "BTC-GBP"
		}

		ETH_BTC_size = round(BTC_GBP_size / ETH_BTC_bid, 8)
		ETH_BTC_params = {
			"size": ETH_BTC_size,
			"price": ETH_BTC_bid,
			"side": "buy",
			"product_id": "ETH-BTC"
		}

		ETH_GBP_params = {
			"size": ETH_BTC_size,
			"price": ETH_GBP_ask,
			"side": "sell",
			"product_id": "ETH-GBP"
		}

		return self.order(BTC_GBP_params, ETH_BTC_params, ETH_GBP_params)

	def order2(self, ETH_GBP_bid, ETH_BTC_ask, BTC_GBP_ask):
		ETH_GBP_size = round((0.002 * BTC_GBP_ask) / ETH_GBP_bid, 8)
		ETH_GBP_params = {
			"size": ETH_GBP_size,
			"price": ETH_GBP_bid,
			"side": "buy",
			"product_id": "ETH-GBP"
		}

		ETH_BTC_params = {
			"size": ETH_GBP_size,
			"price": ETH_BTC_ask,
			"side": "sell",
			"product_id": "ETH-BTC"
		}

		BTC_GBP_size = round(ETH_GBP_size * ETH_BTC_ask, 8)
		BTC_GBP_params = {
			"size": BTC_GBP_size,
			"price": BTC_GBP_ask,
			"side": "sell",
			"product_id": "BTC-GBP"
		}

		return self.order(ETH_GBP_params, ETH_BTC_params, BTC_GBP_params)
