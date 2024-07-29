#server tester
import requests

print("||",'_______________'"||")
print("\/ ENTER URL HERE \/")
URL = input()
r = requests.get(URL,'/get')

print(r.status_code)

if (r.status_code) == 200:
    print("Connection made!")
if (r.status_code) == 201:
    print("Connection made, a new URL had been made to continue with!")
if (r.status_code) == 204:
    print("Connection made, but no content to show")
if (r.status_code) == 301:
    print("Connection made and redirected this URL is no longer valid")
if (r.status_code) == 302:
    print("Connection made, but is using a temporary URL")
if (r.status_code) == 304:
    print("Connection made, this URL has not been modified since last status check")
if (r.status_code) == 400:
    print("No Connectiom, bad sytax, user error with unknown goal")
if (r.status_code) == 401:
    print("Connection made, authorization needed")
if (r.status_code) == 403:
    print("Connection made, but non authorized acess to content")
if (r.status_code) == 404:
    print("No Connection, cannot find URL")
if (r.status_code) == 405:
    print("Connection made, but no allowed acess to content from this source")
if (r.status_code) == 500:
    print("No connection, uknown issue on servers side")
if (r.status_code) == 502:
    print("No connection second source returned an invalid respone, proxy?")
if (r.status_code) == 503:
    print("No connection, server cannot handle this request")



    