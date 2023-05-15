from tkinter import *
from datetime import datetime
from PIL import Image,ImageTk

def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("New user tracking session @" + str(startdatetime))

#Create an instance of tkinter frame
root = Tk()

#Set the geometry of tkinter frame
root.geometry("300x500")

#Create a canvas
canvas= Canvas(root, width= 400, height= 200)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("Logo.png").resize((300,200)))

#Add image to the Canvas Items
canvas.create_image(1,1,anchor=NW,image=img)

import subprocess


def run_program():
    subprocess.call(["python", "Hi-fi (questionnaire).py"])


btn = Button(root, text='Questionnaire', command=run_program)
btn.pack()
logaction(" Questionnaire was selected @" + str(startdatetime))

btn2 = Button(root, text='Fast track (less accurate)')
btn2.pack()


root.mainloop()