import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server_socket.bind((host,port))
server_socket.listen(10)

while 1:
	client_socket,addr = server_socket.accept()
	print "Got a connection from %s" % str(addr)
	cur_time = time.ctime(time.time()) + "\r\n"
	client_socket.send(cur_time.encode('ascii'))
	client_socket.close()
