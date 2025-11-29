import logging
import queue
from logging.handlers import QueueHandler, QueueListener
from src.log_engine.rotation import rotation_handler as get_rotation_handler

def create_fast_logger(config):
    q = queue.Queue(-1)
    logger = logging.getLogger("FastLogger")
    logger.setLevel(getattr(logging, config.level))

    handler = get_rotation_handler(config)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    ))

    listener = QueueListener(q, handler)
    listener.start()

    logger.addHandler(QueueHandler(q))
    return logger
