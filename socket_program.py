#!/usr/bin/python
import socket
import sys

ip = sys.argv[1]
port = sys.argv[2]
socket.setdefaulttimeout(5)

s = socket.socket()
try:
    s.connect((ip,int(port)))
    reply = s.recv(1024)
    print reply
except Exception,e:
	print str(e)

