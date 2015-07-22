import socket
import time
from threading import Thread
from threading import Semaphore
from socket import *
screenlock = Semaphore(value=1)
setdefaulttimeout(2)
def scanPort(ip,port):
        try:
                        if threading.count() > 50:
                                time.sleep(10)
                        else:
                                s=socket(AF_INET, SOCK_STREAM)
                                s.connect((ip,port))
                                s.send("Wow... Port open")
                                screenlock.acquire()
                                print "Port " , port , " open on " , ip
                                print s.recv(1024)
                                print "#########################################################"
                                s.close()
        except Exception,e:
                return
        finally:
                screenlock.release()
def main():
        p=0
        while p < 10000:
                t = Thread(target=scanPort, args=("172.25.30.197",p))
