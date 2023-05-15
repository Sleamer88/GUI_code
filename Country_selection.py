from tkinter import *
from tkinter import ttk
from datetime import datetime
import subprocess

def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("User started selecting country @" + str(startdatetime))

root = Tk()
root.geometry("300x500")
root.title("Select country")

category = Canvas(root,width=300, height=50)
category.pack()
o_category = category.create_oval(2,2,298,48)
t_category = category.create_text(148,23, text="Party/Clubbing")

frame = Frame(root)
frame.pack()

Label(frame, text="Where would you like to visit?").pack()

vlist = ["Netherlands"]
xlist = ["Amsterdam"]



Combov = ttk.Combobox(frame, values= vlist)
Combov.set("Choose a country")
Combov.pack()

Combox = ttk.Combobox(frame,values= xlist)
Combox.set("Choose a city")
Combox.pack()

# Import Required Library
from tkcalendar import Calendar

Label(frame, text="When would you like to visit?").pack()

cal = Calendar(root, selectmode='day',
               year=2020, month=5,
               day=22)

cal.pack()


def grad_date():
    date.config(text="Selected Date at Amsterdam is: " + cal.get_date())


# Add Button and Label
Button(root, text="Get Date", command=grad_date).pack()
logaction(" User selected a date@" + str(startdatetime))

date = Label(root, text="")
date.pack()


Combov.pack()

def run_program():
    logaction(" User has selected location and time for visit@" + str(datetime.now()))
    logaction(" User selected country:" + str(Combov.get()))
    logaction(" User selected city:" + str(Combox.get()))
    logaction(" User selected date:" + str(cal.get_date()))
    root.destroy()
    subprocess.call(["python", "Options.py"])


btn = Button(root, text='Next', command=run_program)
btn.pack()

root.mainloop()
