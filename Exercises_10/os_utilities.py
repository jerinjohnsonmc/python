"""
os_utilities.py  : data logging
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"
import platform
import psutil 

def detect_os()->str:
    # Detect the OS in use
    return platform.system()
    
def cpu_load():
    # Return significant numbers relating to the CPU
    #print(f"Number of CPUs: {psutil.cpu_count()}" )
    #print(f"CPU load: {psutil.cpu_percent()}")
    return(psutil.cpu_count(), psutil.cpu_percent())

if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    
    # Check the OS in use, lower case
    my_os = detect_os()
    my_os = my_os.lower()
    
    # Parse the response
    if my_os == "windows":
        print("Your system is Windows")
    elif my_os == "linux":
        print("Your system is Linux")
    elif my_os == "darwin":
        print("Your Apple system is MacOS")
    elif my_os == "cygwin":
        print("Your Apple system is MacOS")
    elif my_os == "aix":
        print("Your IBM system is AIX")
    else:
        print(f"Unidentified system = {my_os}")
else:
    pass
    #print(f"This module is called {__name__} and is being called by another script")
