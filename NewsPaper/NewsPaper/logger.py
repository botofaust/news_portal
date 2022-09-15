import logging


class LevelFilter(logging.Filter):
    """
    Определяем уровень записи логгера
    """
    def __init__(self, levelno):
        self.levelno = levelno

    def filter(self, record):
        return record.levelno == self.levelno
