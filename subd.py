import requests
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <domain name>")
    sys.exit(1)

#Read the subdomain file and slpit the content by new lines
sub_list = open("subdomains-10000.txt").read()
subs = sub_list.splitlines()

for subd in subs:
    #Construct the url
    url = f"http://{subd}.{sys.argv[1]}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        pass 
    else:
        print("Valid domain: ",url)
