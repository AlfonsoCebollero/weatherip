import logging


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(module)s - %(''levelname)s - %(message)s',
                                  datefmt='%d-%b-%y %H:%M:%S')
    handler = logging.FileHandler('logs.log')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
