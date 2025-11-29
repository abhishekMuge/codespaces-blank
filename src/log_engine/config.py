
class LogConfig:
    def __init__(
        self,
        log_dir: str = "logs",
        file_name: str = "app.log",
        rotation_type: str = "size",
        max_bytes: int = 10 * 1024 * 1024,  # 10 MB
        backup_count: int = 5,
        log_level: str = "INFO",
        when: str = "midnight",
        interval: int = 1,
        formatter_type: str = "text",
    ):
        self.log_dir = log_dir
        self.file_name = file_name
        self.rotation_type = rotation_type
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.log_level = log_level
        self.when = when
        self.interval = interval
        self.formatter_type = formatter_type