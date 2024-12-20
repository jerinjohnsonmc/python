"""
mc_client.py  : multicast  client
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"

import socket
import time
from datetime import datetime
import settings.mc as settings

# Set multicast information
MCAST_GRP = settings.MCCLIENT["MCAST_GROUP"]
MCAST_PORT = settings.MCCLIENT["PORT"]
MCAST_IF_IP = settings.MCCLIENT["IP_ADDRESS"]

print(f'This is the client, make sure its IP address matches {MCAST_IF_IP} in settings.')
print(f'This selects which interface is used for multicast to {MCAST_GRP}.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        # inet_aton converts IPv4 from the a dotted decimal string to 32 bit packed binary format
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(MCAST_GRP) + socket.inet_aton(MCAST_IF_IP))
        message_text = "Ridiculus multicast message"
        message = message_text.encode('utf-8')
        s.sendto(message, (MCAST_GRP, MCAST_PORT))
        print(f'Sent {message_text} to {MCAST_GRP}:{MCAST_PORT}')
        time.sleep(1)