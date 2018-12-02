import sys

reload(sys)
sys.setdefaultencoding('utf8')

import hmac, hashlib, time, base64
from requests.auth import AuthBase


class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.__secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.__api_key,
            'CB-ACCESS-PASSPHRASE': self.__passphrase,
            'Content-Type': 'application/json'
        })

        return request
