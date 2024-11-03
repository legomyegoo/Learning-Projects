import requests

Input_File = input('File Path:')
x = 0
https = 'http://'
with open(OG_proxy_file, 'r') as file:
        print('File List Opened')
        Good_IP_List = []  
        for lines in file:
                linestripped = lines.strip()
                x += 1
                try:
                     r = requests.get(https+linestripped, timeout=1)
                     if r.status_code == 200:
                           Good_IP_List.append(linestripped)
                           print('Good IP')
                except requests.RequestException as e:
                     print('Bad IP')
                    
                if x >= 14: #<- set list # maximum here
                       print('Loop Broke')
                       for ip in Good_IP_List:
                             print(ip)
                       break
                       
