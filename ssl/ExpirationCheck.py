#!/user/bin/env python3
'''
Meta writer test - SSL expiration check using OpenSSl from Bash
'''
import os

site = input("Enter a site url: ")

def writer():
    val = ("echo Name " + site)
    t = ("echo | openssl s_client -servername " + site + " -connect " + site + ":443 2>/dev/null | openssl x509 -noout -dates")
    stream = os.system(str(t))
    return stream 
    
writer()
