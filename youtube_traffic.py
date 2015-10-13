import threading
import os
import subprocess
import time


class URLOpener():
        def __init__(self, url, sno):
                self.url = url
                self.sno = sno
        def start(self):
                print "Process serial no" + str(self.sno)
                subprocess.Popen('service tor restart',shell=True)
                time.sleep(40)
                url='proxychains firefox --private-window ' + self.url
                subprocess.Popen(url,shell=True)
                time.sleep(60)
i=0
while i<5:
        opener = URLOpener('https://www.youtube.com/watch?v=k4YRFOQGnkw',i)
        opener.start()
        pids=os.system("ps -aef | grep chromium-browser | awk '{ print $2 }'")
        print pids
        pids_array = str(pids).split("\n")
        print pids_array
        for id in pids_array:
                print id
                if int(id) != 0:
                        os.system('kill -9 '+ str(id))
        print " chromium-browser got killed after 3 mins"
        i=i+1
