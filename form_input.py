import requests
from bs4 import BeautifulSoup

def actionUrl(baseUrl,ac):
 act=ac
 result=''
 if act.startswith("http") or act.startswith("https"):
  result=act
  return result
 elif act.startswith('/'):
  result=baseUrl[:-1]+act
  return result
 else:
  result=baseUrl
  return result

def get_fieldvalues(htmlForm):
 inputs = htmlForm.find_all('input')
 inputFieldNames = []
 for items in inputs:
    if items.has_attr('name'):
        inputFieldNames.append(items['name'])
 return inputFieldNames

  
def return_input(url):
 request = requests.get(url)
 req=[]
 parseHTML = BeautifulSoup(request.text, 'html.parser')
 forms=parseHTML.find_all('form')
 for form in forms:
  htmlForm = form
  action=''
  method=''
  data={}
  if form.has_attr('action'):
   action=actionUrl(url,form['action'])
  if form.has_attr('method'):
   method=form['method']
  data=get_fieldvalues(form)
  formTextArea=htmlForm.findAll('textarea')
  if not len(formTextArea)==0 :
   data.append(formTextArea[0]['name'])
  req.append(action)
  req.append(method)
  req.append(data)
 return req

#print(return_input('http://testphp.vulnweb.com/signup.php'))
  

  
