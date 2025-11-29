import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

def rotation_handler(config):
    log_path = os.path.join(config.log_dir, config.file_name)

    if(config.rotation_type == "size"):
        return RotatingFileHandler(
            log_path,
            maxBytes=config.max_bytes,
            backupCount=config.backup_count
        )
    elif(config.rotation_type == "time"):
        return TimedRotatingFileHandler(
            log_path,
            when=config.when,
            interval=config.interval,
            backupCount=config.backup_count
        )
    else:
        raise ValueError("Invalid rotation type specified in configuration.")   