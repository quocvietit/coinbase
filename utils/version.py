import sys

# Reload system and get default encoding
reload(sys)
sys.setdefaultencoding('utf-8')

import datetime as dt


def get_date_version():
    # Get date now
    date = dt.datetime.now()

    # Mapping date to date format
    day = "{}{}".format(date.day / 10, date.day % 10)
    month = "{}{}".format(date.month/10, date.month%10)
    year = str(date.year)

    return "-".join([day, month, year])
