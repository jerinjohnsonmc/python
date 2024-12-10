
"""
tcp_client.py  : tcp client
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
import settings.tcp as settings

TCP_IP = settings.TCP["SERVER_TCP_IPv4"]
TCP_PORT = settings.TCP["SERVER_PORT"]

print(f'This is the TCP client, it will try to connect to a server at {TCP_IP}:{TCP_PORT} in the settings file.')
print('This script has no error handling, by design')

BUFFER_SIZE = 1024
while True:
    print(f'Trying to open a socket to {TCP_IP}:{TCP_PORT}')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        message_text = "Jerin says Hi with more reliability"
        message = message_text.encode('utf-8')
        s.connect((TCP_IP, TCP_PORT))
        s.send(message)
        print(f'Sent {message_text} to {TCP_IP}:{TCP_PORT}')
        data = s.recv(BUFFER_SIZE)
        print('Server echoed:', data)
        time.sleep(1)