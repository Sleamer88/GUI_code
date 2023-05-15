from tkinter import *
from datetime import datetime
import subprocess


def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("user opened info on club @" + str(startdatetime))

root = Tk()
root.title("Frame for window")
root.geometry("300x500")
root.config(bg="white")

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

tool_bar = Frame(left_frame, width=180, height=185, bg="grey")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

Label(left_frame, text="Account overview").grid(row=1, column=0, padx=5)

Label(tool_bar, text="Name: AIR Amsterdam").grid(row=0, column=0, padx=5, pady=5)
Label(tool_bar, text="Address: Amstelstraat 24 \n 1017 DA Amsterdam").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Phone: 020 820 0670").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Opening hours: Mon-Wed: closed \n Thurs-Sun: 22:00 - 05:00").grid(row=4, column=0, padx=5, pady=5)
Label(tool_bar, text="Service options: Dine in \n no takeaway, no delivery").grid(row=5, column=0, padx=5, pady=5)


def run_program():
    root.destroy()
    subprocess.call(["python", "Questionnaire(after_experience).py"])


btn = Button(root, text='Next', command=run_program)
btn.grid()

root.mainloop()
