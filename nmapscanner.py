import nmap
import sys

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <target ip>")
    sys.exit(1)

target = str(sys.argv[1])
ports = [20,21,22,23,53,80,139,443,8080]
scan_v = nmap.PortScanner()

print("\nScanning ",target," for ports 20,21,22,23,53,80,139,443,8080...\n")

for port in ports:
    portscan = scan_v.scan(target,str(port)) 
    print("Port ",port," is ",portscan['scan'][target]['tcp'][port]['state'])
    
print("\nHost ",target," is ",portscan['scan'][target]['status']['state'])



