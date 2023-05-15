from tkinter import *
from tkinter import ttk
from datetime import datetime

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
root.geometry("250x400")

def exit_program():
   root.destroy()

#Title frame
title_frame = Frame(root, width=300, height=100)
title_frame.grid(row=0, sticky="wens")

Label(title_frame, text="Here are some revised options \n for your next holiday:").grid(row=1, column=0, padx=20, pady=10, sticky="wens")

#Create a canvas object
circle_canvas = Canvas(root,width=500, height=400)
circle_canvas.grid(row=2, rowspan= 10, sticky="n")

#Draw an Oval in the canvas

c_historical = circle_canvas.create_oval(64,4,164,104)
c_adventurous = circle_canvas.create_oval(4,89,114,199)
c_escape = circle_canvas.create_oval(114,89,214,189)
c_party = circle_canvas.create_oval(64,189,204,329)

t_historical = circle_canvas.create_text(114,54, text="Historical")
t_adventurous = circle_canvas.create_text(59,144, text="Adventurous")
t_escape = circle_canvas.create_text(164,139, text="Escape")
t_party = Button(circle_canvas, text="Party/Clubbing", command=root.destroy).grid(padx=94, pady=249)
logaction(" User is finished with the experience@" + str(startdatetime))

root.mainloop()