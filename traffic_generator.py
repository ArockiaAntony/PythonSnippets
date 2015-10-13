#Opening URL "http://172.25.30.197/Summit_WebLogin.aspx"
import threading
import time
import requests

class StartURLOpener(threading.Thread):

    def __init__(self,url,threadID, noftimes):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.noftimes = noftimes
        self.url = url
    def run(self):
        i=0
        while i < int(self.noftimes):
            try:
                with requests.Session() as session:
                    payload = {'txtLogin':'test', 'txtPassword':'test', 'butSubmit':'SIGN IN'}
                    req = requests.get(str(self.url), auth=('P00112358','ArockTechie1!'))
                    req = session.post(str(self.url))
                    res = req.status_code
                    print res
                    print req.text
                    if int(res) == 200:
                        print "Successfully connected from threadID is " + str(self.threadID) + " run id is " + str(i)
                    else:
                        print "Error in opening url " + str(self.url) + " from threadID " + str(self.threadID)
                    i=i+1
            except Exception as e:
                print "Error in opening url " + str(self.url) + " from threadID " + str(self.threadID)
                print str(e)
                i=i+1

threads = []
thread1 = StartURLOpener("http://arock.in/,100,1)
thread2 = StartURLOpener("http://arock.in/,200,1)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

print threads

for t in threads:
    t.join()
print "Exting main thread"
