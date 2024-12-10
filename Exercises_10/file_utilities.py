
"""
file_utilities.py  : data logging template
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"



from datetime import datetime as dt
import sys, csv

def path_name():
    # Operating system dependent stuff
    this_os = sys.platform
    if this_os == 'win32':
        return './logfiles/'
    elif this_os == 'linux':
        return '/home/pi/logfiles/'
    else:
        print(f'Unsupported OS: {this_os}')
        exit(0)

def log_file_name(extension):
    """
    Create a file name in the logfiles directory, based on current data and time
    Requires the computer to have an RTC or synched clock
    """
    now = dt.now()
    
    current_time = now.strftime("%H-%M-%S")  
    current_date = now.strftime("%Y-%m-%d") 
    # Linux
    file_name = "mylog_" + current_date + "_" + current_time
    return file_name + extension

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    log_path = path_name()
    filename = log_file_name(".log")
    print(log_path + filename )
else:
    pass
    #print(f"This module is called {__name__} and is being called by another script")
