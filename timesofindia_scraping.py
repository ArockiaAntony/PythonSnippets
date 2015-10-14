import requests
from bs4 import BeautifulSoup
import subprocess
import threading
import pynotify
import sys

top_stories_url="http://timesofindia.indiatimes.com/"

top_stories_req = requests.get(top_stories_url)


class ShowNotification(threading.Thread):

	def __init__(self,notificationText,Appname):
		threading.Thread.__init__(self)
		self.text=notificationText
		self.Appname = Appname

	def run(self):
		if not pynotify.init("TOI Notification"):
			pynotify.init(self.Appname)
		n=pynotify.Notification(self.Appname,self.text)
		n.show()

soup = BeautifulSoup(top_stories_req.text)

top_stories = soup.find('ul', attrs={"data-vr-zone":"top_stories"})

notification_array=[]
#fetch top_stories
for top in top_stories:
	c_soup = BeautifulSoup(str(top))
	links=c_soup.findAll('a')
	for link in links:
		#print link.text + "$$$" + link.attrs['href']
		if link.attrs['href'].startswith('/'):
			notification_array.append(link.text)
			#print link.text + "$$$" + top_stories_url + link.attrs['href']
		else:
			notification_array.append(link.text)
			#print link.text + "$$$" + link.attrs['href']

latest_stories = soup.find('ul', attrs={"data-vr-zone":"latest"})

#fetch latest news
for latest in latest_stories:
	c_soup = BeautifulSoup(str(latest))
	links=c_soup.findAll('a')
	for link in links:
		#print link.text + "$$$" + link.attrs['href']
		if link.attrs['href'].startswith('/'):
			notification_array.append(link.text)
		else:
			notification_array.append(link.text)

thread_list=[]
i=0
#for link in notification_array:
#	print link
while i < len(notification_array):
	note_text="-------------------------------------------------------------------" + "\n"
	for v in notification_array[i:i+3]:
		note_text=note_text+ v + "\n" + "-------------------------------------------------------------------" + "\n"
	t_name = ShowNotification(note_text,'TOI Alert')
	t_name.start()
	thread_list.append(t_name)
	i=i+3

for thread in thread_list:
	thread.join()
