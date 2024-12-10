


"""
system_logging.py  : system  logging
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

import logging
from datetime import datetime as dt
today = dt.now()
current_time = today.strftime("%H:%M:%S")  
current_date = today.strftime("%Y-%m-%d") 
logging.basicConfig(level=logging.INFO)


logging.debug('Debug message')
logging.info('Information message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')

file_name = "mylog_" + current_date + "_" + current_time
print (file_name)