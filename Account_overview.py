from tkinter import *
from datetime import datetime


def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("New user tracking session @" + str(startdatetime))

root = Tk()
root.title("Frame for window")
root.geometry("150x250")
root.config(bg="white")

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

tool_bar = Frame(left_frame, width=180, height=185, bg="grey")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

Label(left_frame, text="Account overview").grid(row=1, column=0, padx=5)

Label(tool_bar, text="Name: Dan").grid(row=0, column=0, padx=5, pady=5)
Label(tool_bar, text="Email: dantheman@gmail.com").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Gender: Male").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Occupation: Construction Worker").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Age: 38").grid(row=5, column=0, padx=5, pady=5)


import subprocess

def run_program():
    subprocess.call(["python", "Country_selection.py"])


btn = Button(root, text='Next', command=run_program)
btn.grid()

root.mainloop()
