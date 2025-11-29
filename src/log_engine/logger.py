import logging
import os
from log_engine.rotation import rotation_handler
from log_engine.json_formatter import JsonFromatter

def create_logger(config):
    if not os.path.exists(config.log_dir):
        os.makedirs(config.log_dir)

    logger = logging.getLogger("AppLogger")
    logger.setLevel(getattr(logging, config.log_level.upper(), logging.INFO))

    handler = rotation_handler(config)
    if(config.formatter_type == "json"):
        formatter = JsonFromatter()
    else:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger