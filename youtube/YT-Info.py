#!/usr/bin/env python3

'''
Youtube script - Misc Functions - Sauce: https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
'''
import time
from pytube import YouTube

#link = "https://youtu.be/aTPwbVqU6lc"

#Links for testing 
links = ["https://www.youtube.com/watch?v=B1IsCbXp0uE","https://www.youtube.com/watch?v=48sCx-wBs34", "https://www.youtube.com/watch?v=kJGupYFaCGs"]

for link in links:
    yt = YouTube(link)
    print("Ttile:", yt.title)
   
   #Number of views of video
    print("Number of views: ",yt.views)
   
   #Length of the video
    print("Length of video: ",yt.length, "seconds")
   
   #Description of video
    #print("Description: ",yt.description)
    
    #Rating
    print("Ratings: ",yt.rating)
    print("=-=-=-=-=-=-=-=-=" * 4)
