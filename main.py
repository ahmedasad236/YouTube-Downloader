'''Downloading youtube videos'''
from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
from rich import print
from rich.console import Console
from signal import signal,SIGINT 
import sys
from rich.panel import Panel
from PyInquirer import  prompt
import downloader as dl

running = True      #for the program flow
#program flow
while running == True:
    signal(SIGINT, dl.handler)
    q = list(prompt(dl.questions_2).values())[0] #Select an operation
    test = False   #check the choice
    # TODO USE PyInqureier
    if q == "Go to Downloader" or q == "Exit":
        test = True

    while test == False:
        print("Invalid choice :(")
        q = list(prompt(dl.questions_2).values())[0] #Select an operation
        if q == "Go to Downloader" or q == "Exit":
            test = True

    if q == "Go to Downloader":
        link = list(prompt(dl.questions).values())[0]

        #Check The validity of the Link
        if "https://www.youtube.com" not in link:
            print("Error: Invalid Link :(")

        else:
            # Download a plyalist
            if "playlist" in link:
                dl.Download_playlist(link)

            # Download only one video
            else:
                try:
                    video = YouTube(link)
                    
                except VideoUnavailable:
                    print(f'Video {video.url} is unavaialable')
                else:
                    #video's information
                    dl.video_info(video)
                    
                    # Printing what he wants
                    char = input("v --> vidoes only \na --> audios only \nb --> both\n:")

                    dl.print_what_he_want(video, char)

                    #download his selection
                    dl.Download_video(link)

                    #Asking for continuing
                    choice = input("Download anything else?(y/n)")
                    if choice == "y" or choice == "Y" or choice == "YES".lower():
                        running = True
                    else:
                        running = False
    else:
        print("------------ Thank you :) --------------")
        running = False

    
