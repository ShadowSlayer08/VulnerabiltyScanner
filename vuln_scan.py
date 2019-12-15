import subdomain_takeover
import check_ssrf
import check_sql
import sensitive_data
import xss_check
import check_host_header
import cors
import secrity_header
import check_xxe
#import scrapping
import scraping
import os
from termcolor import colored
import sys

def printBanner():
 cmd="figlet -w 100 'Crawler'"
 returned_value=os.system(cmd)

printBanner()
scraping.crawler(sys.argv[1], 'demofile.txt', '')

def printBanner1():
 cmd="figlet -w 100 'Vulnerability Scanner'"
 returned_value=os.system(cmd)

printBanner1()

def select(a):
	

 if a==1:
  print(colored('Checking XSS','green'))
  xss_check.xsss()
 elif a==2:
  print(colored('Checking SQL Injection','green'))
  check_sql.sqli()
 elif a==3:
  print(colored('Checking XXE','green'))
  check_xxe.xxe()
 elif a==4:
  print(colored('Checking SSRF','green'))
  check_ssrf.ssrf()
 elif a==5:
  print(colored('Checking CORS','green'))
  cors.check_cors(sys.argv[1])
 elif a==6:
  print(colored('Checking Missing Security Headers ','green'))
  secrity_header.check_secruity_headers(sys.argv[1])
 elif a==7:
  print(colored('Checking subdomain_takeover ','green'))
  subdomain_takeover.check_subdomain(sys.argv[1])
 elif a==8:
  print(colored('Checking Sensitive Data Leak ','green'))
  sensitive_data.check_sensitive(sys.argv[1])
 elif a==9:
  print(colored('Checking Host Header Injection ','green')) 
  check_host_header.check_host(sys.argv[1])
 elif a==0:
  print(colored('Exiting  ','red'))
  sys.exit()


def menu():
 print()
 print(colored('1. XSS ','blue'))
 print(colored('2. SQL Injection ','blue'))
 print(colored('3. XXE ','blue'))
 print(colored('4. SSRF ','blue'))
 print(colored('5. CORS ','blue'))
 print(colored('6. Missing Security Headers ','blue'))
 print(colored('7. subdomain_takeover ','blue'))
 print(colored('8. Sensitive Data Leak ','blue'))
 print(colored('9. Host Header Injection ','blue'))
 print(colored('0. Exit ','red'))
 print()
 print(colored('Enter your choice','green'))
 try:
  a=int(input())
  select(a)
 except:
  print(colored('Enter correct option','blue'))
  sys.exit()

menu()
