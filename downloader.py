import random
import urllib.request
from tkinter import *



def Downloader(url):
    name = random.randrange(1,10000)
    filename = str(name) + '.' + extent 
    urllib.request.urlretrieve(url,filename)

base = Tk()
base.title("Downloader")

heading = Label(base, text="Enter Your File type")
heading.pack()
enterText = Entry(base,exportselection=0)
enterText.pack()

SubHeading = Label(base, text="Paste Your URL")
SubHeading.pack()
enterURL = Entry(base,exportselection=0)
enterURL.pack()

extent = enterText.get()
url = str(enterURL.get())

okay = Button(base ,command=lambda: Downloader(url) ,text="Download")
okay.pack()


base.mainloop()
