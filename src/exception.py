'''
CustomException short description:
-Creating a CustomException allows defining and managing specific exceptions for customized situations in the code, enhancing code clarity and maintainability.

Short description of the library used:
-Python's sys library facilitates interaction with the interpreter, managing command arguments, input/output flow, and program termination.
-Python logging library provides a flexible and configurable way to log messages of varying severity levels, aiding in debugging and application monitoring.

'''
# Importing the sys and logging libraries
import sys
from src.logger import logging

# Creating custom error message
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error ocurred in python script name [{0}] line number [{1}] error message[{2}]'.format(
     file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
       super().__init__(error_message)
       self.error_message = error_message_detail(error_message, error_detail = error_detail)
       
    def __str__(self):
        return self.error_message
        