import requests
from bs4 import BeautifulSoup

def check_cors(website):
 try:
  req=requests.get(website,headers={'Origin':'https://bing.com'})
  header=req.headers
  if 'Access-Control-Allow-Origin' in header:
   if header['Access-Control-Allow-Origin']=="*" or header['Access-Control-Allow-Origin:']=='null':
    print("cors vulnerability found on "+website)
 except:
  pass

check_cors('http://testphp.vulnweb.com/')