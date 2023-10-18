import logging
from pythonjsonlogger import jsonlogger

# Create a JSON logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = jsonlogger.JsonFormatter()

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)

file_handler = logging.FileHandler(filename='employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Employee:
    def __init__(self, firstname, lastname) -> None:
        self.fname = firstname
        self.lname = lastname
        logger.info('Created Employee: {} - {}'.format(self.fname,self.lname))    
    
    @property
    def gmail(self):
        return '{}.{}@gmail.com'.format(self.fname,self.lname)
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
emp_1 = Employee('Atique', 'Ahmad')