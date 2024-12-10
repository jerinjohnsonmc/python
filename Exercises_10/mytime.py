
"""
mytime.py  : logging
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
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

current_time = today.strftime("%H:%M:%S")  
current_date = today.strftime("%Y-%m-%d") 

print(f"Current Time: {current_time}")
print(f"Current Date: {current_date}")
