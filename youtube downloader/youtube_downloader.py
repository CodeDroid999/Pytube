#you    should  the   following  libraries installed



from telnetlib import LOGOUT
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.video.io import VideoFileClip
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

#functions
def select_path():
    #allows user to select download path from file explorer
    path= filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path 
    get_link= link_field.get()
    #get selected path 
    user_path= path_label.cget("text")
    screen.title("Downloading...")
    #download video 
    mp4video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(mp4video)
    vid_clip.close
    #move file to selcted directory 
    shutil.move(mp4video, user_path)
    screen.title("Download complete!...Download another video")

screen=Tk()
title=screen.title("YouTube Downloader")
canvas = Canvas(screen,width=500,height=600)
canvas.pack()

#imagelogo
logo_image=PhotoImage(file='yt.png')

#resize the image
logo_image=logo_image.subsample(3,3)
canvas.create_image(250,180,image=logo_image)

#link field
link_field=Entry(screen,width=50)
link_label=Label(screen,text='Enter YouTube video link: ',font="arial,font=15")

#select path to download video
path_label= Label(screen,text='Select download folder',font="arial,font=15")
selct_btn= Button(screen,text='Select',command=select_path)

#add to windows
canvas.create_window(250,420, window=path_label)
canvas.create_window(250,460, window=selct_btn)

#add widgets to window
canvas.create_window(250,330,window=link_label)
canvas.create_window(250,370,window=link_field)

#download buttons
download_btn= Button(screen,text="Download video", command=download_file)

#add buttons to canvas
canvas.create_window(250,500, window=download_btn)
canvas.create_window(250,500, window=download_btn)



screen.mainloop()
