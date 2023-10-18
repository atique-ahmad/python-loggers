import logging
import employee

from pythonjsonlogger import jsonlogger

# Create a JSON logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = jsonlogger.JsonFormatter()

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename='sample.log')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result
    
num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('subtract: {} + {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('multiply: {} + {} = {}'.format(num_1, num_2, mul_result))

divi_result = divide(num_1, num_2)
logger.debug('divide: {} + {} = {}'.format(num_1, num_2, divi_result))
