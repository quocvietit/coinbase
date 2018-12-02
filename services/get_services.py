import setting
import requests

class GetServices:
    def __init__(self, auth):
        self.__auth = auth
        self.__url = setting.URL_PRODUCT

    def product(self, product):
        req = requests.get(self.__url.format(product), auth=self.__auth)

        req_json = req.json()
        bid = float(req_json['bids'][0][0])
        ask = float(req_json['asks'][0][0])
        return (bid, ask)