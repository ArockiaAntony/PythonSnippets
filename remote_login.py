#Author:Arockia Arulnathan
#Date:24-07-2015
#Modified Date:24-07-2015
################################################################################
#Usage:
#1.Create file with host,ip,pwd with "###" seperated in each line.
#Pass the file and cmd which you want to execute in command line.
#Ex: Python remote_execution.py -f "sample.txt" -c "pwd"
#Module Needed: pexpect
################################################################################
import os
import os.path
import optparse
from optparse import OptionParser
import pxssh
import socket

parser = OptionParser()

parser.add_option('-f','--file',dest='FILE',help='Load machines, host, credentials file with # tuple')
parser.add_option('-c','--cmd',dest='CMD',help='Command to load')

(options,args) = parser.parse_args()


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
			print "[+] Connection Error on " , self.host
	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before
def botnet_command(command):
	for client in botNet:
		output = client.send_command(command)
		print "[+] Output  for " , client.host
		print output , "\n"
def add_client(host, user, pwd):
	client = Client(host, user, pwd)
	botNet.append(client)
botNet = []
file = options.FILE
try:
	if os.path.isfile(file):
		f = open(file,'r')
		content = f.readlines()
		for line in content:
			host = line.split("###")[0].strip()
			username = line.split("###")[1].strip()
			password = line.split("###")[2].strip()
			add_client(str(host),str(username),str(password))
		botnet_command(options.CMD)
except Exception, e:
	print str(e)
