import datetime

class Logger:
    """
    Singleton — only one instance ever exists.
    Every call to Logger() returns THE SAME object.
    """
    _instance = None      # narrate: class variable — shared across all instances

    def __new__(cls):
        # narrate: __new__ runs BEFORE __init__; controls object creation
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._logs = []
            cls._instance._level = "INFO"
        return cls._instance   # narrate: always return the same object

    def set_level(self, level: str):
        self._level = level.upper()

    def log(self, message: str, level: str = "INFO"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        self._logs.append(entry)
        print(entry)

    def info(self, message: str):
        self.log(message, "INFO")

    def error(self, message: str):
        self.log(message, "ERROR")

    def get_logs(self) -> list:
        return list(self._logs)   # return a copy — don't expose the internal list