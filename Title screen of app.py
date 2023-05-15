from tkinter import *
from datetime import datetime
from PIL import Image,ImageTk
import subprocess

def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("New user tracking session @" + str(startdatetime))

#Create an instance of tkinter frame
root = Tk()
root.geometry("300x500")
root.title("App")

#Create a canvas
canvas= Canvas(root, width= 400, height= 200)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("./Images/Logo.png").resize((300,200)))

#Add image to the Canvas Items
canvas.create_image(1,1,anchor=NW,image=img)


def open_questionnaire():
    logaction(" Questionnaire was selected @" + str(datetime.now()))
    root.destroy()
    subprocess.call(["python", "Hi-fi (questionnaire).py"])

def skip_questionnaire():
    logaction(" Questionnaire was skipped @" + str(datetime.now()))
    root.destroy()
    subprocess.call(["python", "Bubbles_page.py"])   
    


btn = Button(root, text='Questionnaire', command=open_questionnaire)
btn.pack()


btn2 = Button(root, text='Fast track (less accurate)', command=skip_questionnaire)
btn2.pack()


root.mainloop()