from tkinter import *
from datetime import datetime
from subprocess import call

def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("New user tracking session @" + str(startdatetime))


root = Tk()
root.title("Welcome")


#Define the geometry of window
root.geometry("300x500")


#Title frame
title_frame = Frame(root, width=300, height=100)
title_frame.grid(row=0, sticky="wens")

Label(title_frame, text="Here are some options for your next holiday:").grid(row=1, column=0, padx=20, pady=10, sticky="wens")

#Create a canvas object
circle_canvas = Canvas(root,width=500, height=400)
circle_canvas.grid(row=2, rowspan= 10, sticky="n")

#Draw an Oval in the canvas
c_beach = circle_canvas.create_oval(4,29,64,89)
c_historical = circle_canvas.create_oval(64,4,164,104)
c_city = circle_canvas.create_oval(164,29,204,69)
c_adventurous = circle_canvas.create_oval(4,89,114,199)
c_escape = circle_canvas.create_oval(114,89,214,189)
c_cruise = circle_canvas.create_oval(4,199,64,259)
c_party = circle_canvas.create_oval(64,189,204,329)

t_beach = circle_canvas.create_text(34,59, text="Beach")

t_party = Button(circle_canvas, text="Party/Clubbing", command=Open("Account_overview.py"))

root.mainloop()

#import math
#import tkinter as tk

#def draw(angle, text):
#    x = math.cos(math.radians(angle)) * 50 + 250
#    y = math.sin(math.radians(angle)) * 50 + 250
#    obj = canvas.create_text(250, 250, text=text, fill="green")
#    canvas.itemconfig(obj, angle=-angle)
#    canvas.coords(obj, x, y)
#    return obj

#root = tk.Tk()
#canvas = tk.Canvas(root, width=500, height=500)

#for i in range(0,360,60):
    #draw(i,"Hi")

#canvas.pack()
#root.mainloop()