'''Downloading youtube videos'''
from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable
from rich import print
from rich.console import Console
from signal import signal,SIGINT 
import sys
from rich.panel import Panel
from PyInquirer import  prompt

console = Console() 
def finish():       #trivial function for printing
    print("Download Done :)")

def Downloading():  #trivial function for printing
    print("downloading...")

def bye():
      console.print(Panel.fit('''    [bold red]Thank YOU [/bold red][bold]for using  youtube downloader 
        If you enjoy it, feel free to leave a [/bold][bold red]Star[/bold red]
        [italic bold yellow]https://github.com/ahmedasad236/YouTube-Downloader[/italic bold yellow]
        [italic cyan]Feedback and contribution is welcome as well :smiley:![/italic cyan]
            ''', title="Bye!"), justify="center")


def handler(signal_received, frame):
    # Handle any cleanup here
    print('\n[bold]SIGINT or CTRL-C detected. [red]Exiting gracefully[/red][/bold]')
    bye()
    sys.exit(0)

console.rule("Welcome to Youtube Downloader")
questions = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Enter YouTube Video Url:',
        }
    ]
questions_2 = [
    {
        'type': 'list',
        'name': 'size',
        'message': 'What  do you want?',
        'choices': ["Go to Downloader", "Exit"]
    }
]

#video's information
def video_info(video):
    hours = video.length // 3600
    minutes = (video.length - hours * 3600) // 60
    seconds = video.length - minutes * 60
    print("------------ video information ----------- ")
    print(f"Video Title: \n{video.title}")
    print(f"Video Length: {hours} : {minutes} : {seconds}")
    print(f"Video Views: {video.views}")



# print what user wants
def print_what_he_want(video, char):
    if char == "A".lower():
        for stream in video.streams.filter(only_audio=True):
            print(stream)

    elif char == "V".lower():
        for stream in video.streams.filter(only_video=True):
            print(stream)

    elif char == "B".lower():
        for stream in video.streams.filter(progressive=True):
            print(stream)


# Download his Selection
def Download_selected(video):
    it = input("Enter the itag of your choice:")
    video.streams.get_by_itag(it).download()
    video.register_on_complete_callback(finish())
    video.register_on_progress_callback(Downloading())
    print("-----------------------------------------------")

# Donload a playlist
def Download_playlist(link):
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


def Download_video(link):
    try:
        video = YouTube(link)
    except VideoUnavailable:
        print(f'Video {video.url} is unavaialable')
    else:
        video_info(video)
        char = input("v --> vidoes only \na --> audios only \nb --> both\n:")
        print_what_he_want(video, char)
        Download_selected(video)


