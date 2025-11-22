import logging
import os


logger = None


def get_logger() -> logging.Logger:
    global logger

    if not logger:
        formatter = logging.Formatter('[%(asctime)s] [%(filename)s] [%(lineno)d] [%(levelname)s] %(message)s')

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(os.environ.get('LOG_LEVEL', 'DEBUG'))
        logger.addHandler(ch)

    return logger
