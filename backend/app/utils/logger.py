from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", colorize=True)


def get_logger():
    return logger
