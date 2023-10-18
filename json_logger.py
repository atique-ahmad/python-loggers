import logging
from pythonjsonlogger import jsonlogger

# Create a JSON logger
logger = logging.getLogger('my_json_logger')
logger.setLevel(logging.DEBUG)

formatter = jsonlogger.JsonFormatter()

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
# Log messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
