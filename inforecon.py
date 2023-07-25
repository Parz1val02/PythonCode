import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

#Banner
req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

#Ip: 
gethost_name = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is: " + gethost_name + "\n")

#API for iplookup: ipinfo.io
req_2 = requests.get("https://ipinfo.io/ " + gethost_name + "/json")
response = json.loads(req_2.text)

print("Location: " + response['loc'])
print("Region: " + response['region'])
print("City: " + response['city'])
print("Country: " + response['country'])
