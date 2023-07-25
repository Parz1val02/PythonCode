import random
import os
import subprocess

def get_random():
    return random.choice("abcdef0123456789")

def new_mac():
    new_a=""
    for i in range(0,5):
        new_a+=get_random()+get_random()+":"
    new_a=get_random()+get_random()
    return new_a

print(os.system("ifconfig | grep ether | grep -oE [0-9abcdef:]{17}"))

subprocess.call(["sudo","ifconfig","eth0","down"])

new_m = new_mac()

subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m])

subprocess.call(["sudo","ifconfig","eth0","up"])

print(os.system("ifconfig | grep ether | grep -oE [0-9abcdef:]{17}"))
