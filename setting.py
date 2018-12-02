import os
import sys

# Loger
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Language
LANGUAGE = "english"

# Setup logging
LOGGING_FILE_PATH = os.path.join(DIR_PATH, 'logs')
LOGGING_CONTENT_FORMAT = "%(asctime)s [%(threadName)s] [%(levelname)s] - %(message)s"
LOGGING_DATE_FORMAT = "%d/%m/%Y %I:%M:%S %p"
LOGGING_FILE_NAME_FORMAT = "{}\log-{}.txt"

# URL
URL_ROOT = "https://api.pro.coinbase.com"
URL_PRODUCT = URL_ROOT + "/products/{}/book"
URL_ORDER = URL_ROOT + "/orders"

# API
API_KEY = os.getenv("APP_KEY")
API_SECRET = os.getenv("APP_SECRET")
API_PASS = os.getenv("APP_PASS")
