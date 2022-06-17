from textwrap import fill
import tkinter
from tkinter import *
import tkinter.font as font
from pytube import YouTube
from threading import *
import os

root = tkinter.Tk()
root.title('Youtube MP3 Downloader by tomich')
root.config(bg='#2A0944')


def addLink():
    if not E1.get().strip():    # if empty, so if wont leave empty space in list
        return
    LB1.insert(LB1.size(), E1.get())
    LB2.insert(LB2.size(), YouTube(E1.get()).title)


def download():
    L2.config(text="The download has begun.")
    for x in range(LB1.size()):
        yt = YouTube(LB1.get(x))
        video = yt.streams.filter(only_audio=True).first()
        destination = './Songs'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        L2.config(text=yt.title + " has been downloaded.")
    L2.config(text="The download has finished.")


def threadingDownload():    # runs function on another thread
    # Call download function
    t1 = Thread(target=download)
    t1.start()


def threadingAddLink():     # runs function on another thread
    # Call addLink function
    t2 = Thread(target=addLink)
    t2.start()


# STYLE
buttonFont = font.Font(family='Helvetica', size=10, weight='bold')

L1 = Label(root, text="Link:", font=(
    "Montserrat", 18), bg='#2A0944', fg='#FFFFFF')
L1.grid(row=0, column=0, pady=5)

E1 = Entry(root, bd=1, width=20, font=(
    "Montserrat", 18), bg='#A12568', fg='#FFFFFF')
E1.grid(row=0, column=1)
B1 = Button(root, text="ADD", padx=10, pady=5,
            command=threadingAddLink, bg='#FEC260', fg='#0F0E0E', font=buttonFont)
B1.grid(row=1, column=0)

scrollbar = Scrollbar(root)
scrollbar.grid(row=2, column=2, sticky='ns')

var2 = tkinter.StringVar()
LB2 = tkinter.Listbox(root, listvariable=var2, width=50, height=20, font=(
    "Montserrat", 8), bg='#A12568', fg='#FFFFFF')
LB2.grid(row=2, column=0, pady=5)

var1 = tkinter.StringVar()
LB1 = tkinter.Listbox(root, listvariable=var1, width=50, height=20, font=(
    "Montserrat", 8), bg='#A12568', fg='#FFFFFF')
LB1.grid(row=2, column=1)

LB1.config(yscrollcommand=scrollbar.set)
LB2.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=LB1.yview)
scrollbar.config(command=LB2.yview)


B2 = Button(root, text="Start", padx=10, pady=5,
            command=threadingDownload, bg='#FEC260', fg='#0F0E0E', font=buttonFont)
B2.grid(row=3, column=0)

L2 = Label(root, text="", font=(
    "Montserrat", 10), bg='#2A0944', fg='#FFFFFF', wraplength=300)
L2.grid(row=4, column=0, pady=5)

root.mainloop()
