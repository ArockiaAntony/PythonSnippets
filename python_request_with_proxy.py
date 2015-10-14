import requests
from bs4 import BeautifulSoup

proxy_dic = {"http" : "http://P00112358@asianpaints.com@gateway.zscaler.net:80/",
             "https" : "http://P00112358@asianpaints.com@gateway.zscaler.net:80/"}

url = "http://arock.in"

request = requests.get(url, proxies=proxy_dic)

print request.status_code
soup = BeautifulSoup(request.text)

print soup.prettify()
