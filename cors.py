import requests
from bs4 import BeautifulSoup
from form_urls import *

def check_cors():
 list_of_urls=iterate_through_file('demofile.txt')
 for url in list_of_urls:
  try:
   req=requests.get(url,headers={'Origin':'https://bing.com'})
   header=req.headers
   if 'Access-Control-Allow-Origin' in header:
    if header['Access-Control-Allow-Origin']=="*" or header['Access-Control-Allow-Origin:']=='null':
     print("cors vulnerability found on "+url)
  except:
   pass

#check_cors('http://testphp.vulnweb.com/')