#Mike Tsak 17/10/22

#pip install termcolor
#pip install requests

#import imp
import sys
import requests
import json
from time import sleep
#from termcolor import colored

api_key = ""
domain = ""
password = "x"

headers = { 'Content-Type' : 'application/json' }

def sendmail(mailsent, x, y):
    ticket = {
        'email': mailsent,
        'subject': y,
        'description': x,
        'status': 5,
        'priority': 2,
        'email_config_id': 101000001287,
      }
    r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets/outbound_email", auth = (api_key, password), headers = headers, data = json.dumps(ticket))

    if r.status_code == 201:
      print ("Location Header : ",  r.headers['Location'])
    else:
        print ("Failed to create ticket, errors are displayed below,")
        response = json.loads(r.content)
        print (response["errors"])

        print ("x-request-id : ",  r.headers['x-request-id'])
        print ("Status Code : ", str(r.status_code))
    with open("lastmail.txt", "w") as f:
        f.write(mailsent)

    
  
####MAIN####


print("Email Randomizer! for POPMARKET")
print("Ποσα email βαζεις για imput;")
j = int(input())

print("Ποσα email, θέλεις να στελένεις το λεπτό;")
epm = int(input())
f = open("mails.txt", "r")
mail = f.read().split()
#print("test mail", mail[0])
print("----------------------------")
y = input("Θεμα του email:")
x = input("Το σωμα mail σε HTML:")

waiting =  j/ epm 

print("Θα παρει ", waiting, "λεπτα για να στελει τα ", j, "email")
print("Πατα 1 για να συνεχισεις")
waiting = int(input())

if waiting == 1:
  i = 0
  while i < j:
    sendmail(mail[i], x, y)
    print(mail[i])
    i = i + 1
    sleep(waiting) 



print("Τελος προγραμματος")





