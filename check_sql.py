import requests
from bs4 import BeautifulSoup
import mechanize
from form_urls import *
from form_input import *

payload=['\'','"','\\']
error=['error','exception','illegal','invalid','fail','stack','access','directory','file','not found','varchar','ODBC','SQL','SELECT']
list_of_urls=iterate_through_file('demofile.txt')

def make_req(data,payloa):
 d={}
 for i in data:
  d[i]=payloa
 return d

def checkSqlInjection(res,f):
 flag=False
 for i in error:
  if i in res.text:
   print('Sql injection Found on url:'+res.url)
   print('payload:'+str(f))
   flag=True
   break
 return flag
for i in list_of_urls:
 input_req=return_input(i)
 for k in range(0,len(input_req),3):
  if input_req[k+1]=='post' or input_req[k+1]=='POST':
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.post(input_req[k],d)
    if checkSqlInjection(request,d):
     break

