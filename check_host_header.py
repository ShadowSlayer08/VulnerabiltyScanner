import requests
from bs4 import BeautifulSoup

def check_host(website):
 try:
  req=requests.get(website,headers={'Host':'www.bing.com'})
  if req.status_code==302 or req.status_code==301 or 'www.bing.com' in req.text:
   print('Host header injection found on '+website)

  req=requests.get(website,headers={'X-Forwarded-Host':'www.bing.com'})
  if req.status_code==302 or req.status_code==301 or 'www.bing.com' in req.text:
   print('Host header injection found on '+website)
 except:
 	pass



#check_host('https://core.trac.wordpress.org/ticket/25239')
