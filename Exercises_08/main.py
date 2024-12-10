"""
main.py  : python class demo wiith methods and inheritance
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

from devices import Firewall,Switch

# Create a firewall instance
my_firewall = Firewall("192.168.1.5")
# Configure it
my_firewall.configure_firewall()

# Create a switch instance
my_switch = Firewall("192.168.1.7")
# connect
my_switch.connect("192.168.1.7")