"""
for_ex.py : for loop exercise
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"


scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}



    
for ip_port in scan:
    print(f"Found a service on {ip_port}")
    
    
for ipv4, port in scan.items():
    print(f"Found a service on {ipv4} at {port}")
    
    
