from tkinter import *
from datetime import datetime


def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("Profile opened @" + str(startdatetime))

root = Tk()
root.title("Profile")
root.geometry("300x500")

title_frame = Frame(root, width=200, height=400, pady=10)
title_frame.pack()
Label(title_frame, text="Account overview").pack()


tool_bar = Frame(title_frame, width=180, height=185, bg="grey", pady=10)
tool_bar.pack()

Label(tool_bar, text="Name: Dan ").pack()
Label(tool_bar, text="Email: dantheman@gmail.com ").pack()
Label(tool_bar, text="Gender: Male ").pack()
Label(tool_bar, text="Occupation: Construction worker ").pack()
Label(tool_bar, text="Age: 38 ").pack()


import subprocess

def run_program():
    root.destroy()
    subprocess.call(["python", "Country_selection(proof of concept).py"])


btn = Button(root, text='Next', command=run_program)
btn.pack()

root.mainloop()
