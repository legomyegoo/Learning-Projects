from bs4 import BeautifulSoup
from datetime import time, timedelta, datetime
import time as tm
import requests
import schedule 

print('go')
stream_URL = input('Enter URL: ')
r = requests.get(stream_URL)


#trying to get connection function
def intital_connection_try():
    if r.status_code == 200:
        print('W connection,', r.status_code)
        'intital_connection_attempt' == True
    
    else:
        print('L connection,',  r.status_code)
        'intital_connection_attempt' == False

intital_connection_try()

#countinuing to try connection function
def keep_trying_connection():
        requests.get(stream_URL)
        if r.status_code == 200:
             print('Connection Stable')
             'Connection Stable' == True
             #send to discord
        
        else:
            'Connection Stable' == False
            print('Connection Broken', r.status_code)
            #send to discord
            
             
#if the connection is made keep checking for it ebvery day
if 'intital_connection_attempt' == True:
     keep_trying_connection()
  
def scan_for_new_posts():
    requests.get(stream_URL)
     



if 'Connection Stable' == True:
    scan_for_new_posts()
    








schedule.every(1).days.do(keep_trying_connection)

while True:
    schedule.run_pending()
    tm.sleep(1)
    