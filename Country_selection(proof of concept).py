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
root.geometry("300x580")

category = Canvas(root,width=300, height=100)
category.grid(row=0, rowspan= 2, sticky="n")
o_category = category.create_oval(2,2,298,48)
t_category = category.create_text(148,23, text="Party/Clubbing")

frame = Frame(root)
frame.grid()

Label(frame, text="Where would you like to visit?").grid(row=1, column=0, padx=5)

vlist = ["Netherlands"]
xlist = ["Amsterdam"]



Combov = ttk.Combobox(frame, values= vlist)
Combov.set("Choose a country")
Combov.grid(padx=5, pady=5)
logaction(" User selected a country@" + str(startdatetime))

Combox = ttk.Combobox(frame,values= xlist)
Combox.set("Choose a city")
Combox.grid(padx=6, pady=6)
logaction(" User selected a city@" + str(startdatetime))

# Import Required Library
from tkcalendar import Calendar

Label(frame, text="When would you like to visit?").grid(row=5, column=0, padx=5)

cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)

cal.grid(pady=20)


def grad_date():
    date.config(text="Selected Date at Amsterdam is: " + cal.get_date())


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).grid(pady=20)
logaction(" User selected a date@" + str(startdatetime))

date = Label(root, text="")
date.grid(pady=20)


Combov.grid(padx=5, pady=5)


import subprocess

def run_program():
    subprocess.call(["python", "Options.py"])


btn = Button(root, text='Next', command=run_program)
btn.grid()
logaction(" User has selected location and time for visit@" + str(startdatetime))

root.mainloop()
