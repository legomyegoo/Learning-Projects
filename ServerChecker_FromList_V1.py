import requests

Input_File = input('File Path:')
x = 0
https = 'http://'

with open(Input_File, 'r') as file:
        print('File List Opened')
        for lines in file:
                linestripped = lines.strip()
                print('Read Line')
                x += 1 
                if x >= 5: #set to 5 for test reasons(ex. my list is 300 lines)
                       print('Loop Broke')
                       break
                try:
                    r = requests.get(https+linestripped)
                    if r.status_code == 200:
                           print('Good Connection')
                
                except Exception as e:
                       print('No Connection')
                       continue
                