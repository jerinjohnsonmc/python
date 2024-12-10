"""
main.py : run test project
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

from pkg.directory_utilities import detect_os, detect_working_directory
from mypaths import UDP_SETTINGS as udp_settings
print(detect_os())
print(detect_working_directory())    

print(udp_settings)