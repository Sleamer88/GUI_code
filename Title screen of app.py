from tkinter import *
from datetime import datetime

def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("New user tracking session @" + str(startdatetime))

# root = Tk()
# root.title("Welcome")
#
#
# #Define the geometry of window
# root.geometry("1000x4000")
#
# #Create a canvas object
# c= Canvas(root,width=400, height=400)
# c.pack()
#
# #Draw an Oval in the canvas
# c.create_oval(60,60,210,210)


# from tkinter import PhotoImage
#
# image = PhotoImage(file="test.png")
#
# root = Tk()
# cv = Canvas(root)
# cv.create_image(10,10, image=image)
# cv.pack()
# root.mainloop()


#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x650")

#Create a canvas
canvas= Canvas(win, width= 600, height= 400)
canvas.pack()

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("Logo.png"))

#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=img)

win.mainloop()


