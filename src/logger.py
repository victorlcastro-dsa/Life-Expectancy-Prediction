'''
Short description of logging:
-Logging allows for systematic recording of events, errors, and information during runtime, aiding in debugging, monitoring, and understanding the behavior of an application.


Short description of the libraries used:
-Python logging library provides a flexible and configurable way to log messages of varying severity levels, aiding in debugging and application monitoring.
-Python os library provides functions to interact with the operating system, including operations related to files, directories, and the execution environment.
-Python datetime library provides functionalities to work with dates, times, time zones, and timedeltas, facilitating various operations related to date and time manipulation.

'''

#Importing the logging and os library
import logging
import os
from datetime import datetime

#Creating File, Path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

#Logging basic configuration
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = '[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level = logging.INFO, 
)
