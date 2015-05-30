'''
    Simple socket server
    USE: telnet
'''

import socket
import sys
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is the address family: Address Family IP
# TCP almost always uses SOCK_STREAM and UDP uses SOCK_DGRAM
print 'Socket created'
 
# Bind socket to local host and port
# ora il soket e' in ascolto
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(5)
print 'Socket now listening'
 
# Accept a connection. The return value is a pair (conn, address) 
# where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

while True:
    # wait to accept a connection - blocking call
    # where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
s.close()
