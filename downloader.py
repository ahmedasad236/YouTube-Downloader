#Library for youtube downloader
from pytube import YouTube, Playlist

running = True      #for the program flow

def finish():       #trivial function for printing
    print("Download Done :)")

def Downloading():  #trivial function for printing
    print("downloading...")

print("********* Welcome to Youtube Downloader *********")

#program flow
while running == True:

    print("1- go to downloader")
    print("2- Exit")
    q = input("Your choic: ") #Select an operation
    test = False   #check the choice

    if q == str(1) or q == str(2):
        test = True

    while test == False:
        print("Invalid choice :(")
        q = input("Your choic: ")
        if q == str(1) or q == str(2):
            test = True

    if q == str(1):
        link = input("Enter your Link: ")

        #Check The validity of the Link
        if "https://www.youtube.com" not in link:
            print("Error: Invalid Link :(")

        else:
            # Download a plyalist
            if "playlist" in link:
                plist = Playlist(link)
                print(f'Downloading: {plist.title}')
                for url in plist.video_urls:
                    #check the validity of each video in the list
                    try:
                        yt = YouTube(url)
                    except VideoUnavailable:
                        print(f'Video {url} is unavaialable, skipping.')
                    else:
                        #downloding
                        print(f'Downloading video: {url}')
                        yt.streams.first().download()

            # Download only one video
            else:
                try:
                    video = YouTube(link)
                except VideoUnavailable:
                    print(f'Video {url} is unavaialable')
                else:
                    #video's information
                    hours = video.length // 3600
                    minutes = (video.length - hours * 3600) // 60
                    seconds = video.length - minutes * 60
                    print("------------ video information ----------- ")
                    print(f"Video Title: \n{video.title}")
                    print(f"Video Length: {hours} : {minutes} : {seconds}")
                    print(f"Video Views: {video.views}")
                    char = input("v --> vidoes only \na --> audios only \nb --> both\n:")
                    # Printing what he wants
                    if char == "A".lower():
                        for stream in video.streams.filter(only_audio=True):
                            print(stream)

                    elif char == "V".lower():
                        for stream in video.streams.filter(only_video=True):
                            print(stream)

                    elif char == "B".lower():
                        for stream in video.streams.filter(progressive=True):
                            print(stream)

                    #download his selection
                    it = input("Enter the itag of your choice:")
                    video.streams.get_by_itag(it).download()
                    video.register_on_complete_callback(finish())
                    video.register_on_progress_callback(Downloading())
                    print("-----------------------------------------------")

                    #Asking for continuing
                    choice = input("Download anything else?(y/n)")
                    if choice == "y" or choice == "Y" or choice == "YES".lower():
                        running = True
                    else:
                        running = False
    else:
        print("------------ Thank you :) --------------")
        running = False