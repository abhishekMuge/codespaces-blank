from log_engine.config import LogConfig
from log_engine.logger import create_logger
# from log_engine.fast_logger import create_fast_logger   # use if needed

def main():
    config = LogConfig(
        rotation_type="size",
        max_bytes=1024 * 1024,  # 1MB
        backup_count=3,
        formatter_type="json"
    )

    logger = create_logger(config)

    for i in range(100000000000):
        logger.info(f"Log entry number: {i}")

if __name__ == "__main__":
    main()
