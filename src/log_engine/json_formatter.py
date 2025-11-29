import json
import logging
from datetime import datetime

class JsonFromatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "process": record.process,
            "thread": record.threadName,
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno
        }

        return json.dumps(log_record)