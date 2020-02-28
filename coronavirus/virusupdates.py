#!/usr/bin/env python3

'''
Corona virus (COVID-19) tracker.
'''
import os
import requests
from bs4 import BeautifulSoup

def corona():

    URL = "https://www.worldometers.info/coronavirus/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    #Historical from gen 1
    #results = soup.find('div', class_='maincounter-number')

    dresults = soup.find_all('div', class_='maincounter-number')

    #trying the loop here
    values = []
    for dresult in dresults:
        values.append(dresult.text)

    #Prepare outputs
    print("****" * 13)
    print("⚠️  Current number of Coronavirus cases ⚠️ " + values[0])
    print("❗️ Current number of Coronavirus deaths❗️ " + values[1])
    print("****" * 13)
    os.system("say there are" + values[0] + "current cases of corona virus and" + values[1] + "people have perished.")

corona()
