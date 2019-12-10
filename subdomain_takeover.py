import requests
from bs4 import BeautifulSoup


domains=set()
req=requests.get("https://crt.sh/?q=%25spotify.com")
soup=BeautifulSoup(req.text,features="lxml")
rows=soup.findAll('td')
for i in rows:
 try:
  if i.text.endswith(".com"):
  	domains.add(i.text)
    #domains.add(str(i).split('\n')[5].replace('<td>','').replace('</td>',''))
 except:
 	pass
for i in domains:
 try:
  req=requests.get("http"+i)
  if req.status_code==404 or "Not found" in req.text:
   print("subdomain takeover found on domain"+i)
 except:
   print(i)

