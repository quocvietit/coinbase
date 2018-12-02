import logging
import os.path
from utils.version import get_date_version
import setting


def initialize_logger():
    version = get_date_version()
    log_file = setting.LOGGING_FILE_NAME_FORMAT.format(setting.LOGGING_FILE_PATH, version)

    # Check folder exits
    if not os.path.exists(setting.LOGGING_FILE_PATH):
        os.makedirs(setting.LOGGING_FILE_PATH)

    # Check file exits
    if not os.path.isfile(log_file):
        with open(log_file, "w+") as file:
            file.write(version + "\n")
            file.close()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    format = setting.LOGGING_CONTENT_FORMAT
    datefmt = setting.LOGGING_DATE_FORMAT

    logger.addHandler(handler_log_console(format, datefmt))
    logger.addHandler(handler_log_file(format, log_file))

    logging.info("-----------------------------------------------------------------------------------------------------")


def handler_log_console(format, datefmt):
    formatter = logging.Formatter(format, datefmt)

    handler = logging.StreamHandler()

    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    return handler


def handler_log_file(format, file):
    formatter = logging.Formatter(format)

    handler = logging.FileHandler(file, "a")

    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    return handler
