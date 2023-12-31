#!/usr/bin/python
import socket
import sys
from datetime import datetime as dt

# Define target
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()
else:
    print("Invalid amount of arguments")
    print("Syntax: python scanner.py <ip>")
    sys.exit(0)

print("-" * 20)
print(f"Scanning target: {target}")
print("Time started: " + str(dt.now()))
print("-" * 20)

try:
    for port in range(7770, 7780):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting program ...")
    sys.exit()
except socket.error:
    print("Could not connect to the server")
    sys.exit()
