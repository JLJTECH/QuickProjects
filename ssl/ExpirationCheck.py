#!/user/bin/env python3
'''
SSL expiration check using OpenSSl in Bash
'''
import os

#Take user input URL
site = input("Enter a site url: ")

def writer():
    #Craft the CLI command to run the SSL expiration check
    comm = ("echo | openssl s_client -servername " + site + " -connect " + site + ":443 2>/dev/null | openssl x509 -noout -dates")
    #Run command
    stream = os.system(str(comm))
    return stream 

writer()
