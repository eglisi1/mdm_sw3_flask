import logging

""" This is the logger service. It is used to log messages to the console. """
class Logger:
    def __init__(self, log_level=logging.DEBUG):
        self.log_formatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
        self.root_logger = logging.getLogger()
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.log_formatter)
        self.root_logger.addHandler(self.console_handler)
        self.root_logger.setLevel(level=log_level)

    def info(self, message):
        self.root_logger.info(message)

    def error(self, message):
        self.root_logger.error(message)

    def debug(self, message):
        self.root_logger.debug(message)

    def warning(self, message):
        self.root_logger.warning(message)

    def critical(self, message):
        self.root_logger.critical(message)
