import socket
import time

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect((host,port))

answer = s.recv(1024)

print answer
