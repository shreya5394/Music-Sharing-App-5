import socket 
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from playsound import playsound
import pygame
from pygame import mixer
import ftplib
from ftplib import FTP
import os 
import time
import ntpath
from pathlib import Path

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared/files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared/files/'+song_selected)
    mixer.music.pause()

def musicWindow():
    window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectLabel = Label(window, text="Select Song", bg='LightSkyBlue', font = ("Calibri",0))
    selectLabel.place(x=2, y=1)

    listbox = Listbox(window, height=10, width=39, activestyle='dotbox',bg='LightSkyBlue',borderwidth=2, font = ("Calibri", 10))
    listbox.place(x=10, y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx=1)
    scrollbar1.config(command= listbox.yview)

    PlayButton=Button(window, text="Play", width=10, bd=1, bg='SkyBlue', font = ("Calibri", 10))
    PlayButton.place(x=30,y=200)

    Stop=Button(window, text="Stop", bd=1, width=10, bg='SkyBlue', font = ("Calibri", 10))
    Stop.place(x=200,y=200)

    ResumeButton=Button(window, text="Resume", width=10, bd=1, bg='SkyBlue', font=("Calibri", 10), command = resume)
    ResumeButton.place(x=30,y=250)

    PauseButton=Button(window, text="Pause", width=10, bd=1, bg='SkyBlue', font=("Calibri", 10), command = pause)
    PauseButton.place(x=200,y=250)

    Upload=Button(window, text="Upload", bd=1, width=10, bg='SkyBlue', font = ("Calibri", 10))
    Upload.place(x=30,y=250)

    Download=Button(window, text="Download", bd=1, width=10, bg='SkyBlue', font = ("Calibri", 10))
    Download.place(x=200,y=250)

    infoLabel=Label(window, text="", fg='blue', font = ("Calibri", 10))
    infoLabel.place(x=4,y=280)

    window.mainloop()


def browseFiles():
    global Listbox
    global soung_counter
    global filePathLabel

    try:
        filename = filedialog.askopenfilename()
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"

        ftp_server = FTP(HOSTNAME,USERNAME,PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared-files')
        fname=ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)

        ftp_server.dir()
        ftp_server.quit()

        listbox.insert(soung_counter, fname)
        song_counter = song_counter + 1
    except FileNotFoundError:
        print("Cancel Button Pressed")

def download():
    #textarea.insert(END,"\\n"+"\nPlease wait file is downloading.....")
    #textarea.see("end")

    song_to_download=listbox.get(ANCHOR)
    infoLabel.configure(text="Downloading "+song_to_download)
    HOSTNAME = "127.0.0.1"
    USERNAME = "lftpd"
    PASSWORD= "lftpd"
    home = str(Path.home())
    

def setup():
    
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()

