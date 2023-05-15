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
root.geometry("250x310")
root.title("Questionnaire")

# set up the frames
title_frame = Frame(root, width=250, height=100)
title_frame.grid(row=0, column=0, padx=5, pady=5, sticky="wens")

q1_frame = Frame(root, width=250, height=150)
q1_frame.grid(row=1, column=0, padx=5, pady=5, sticky="wens")

q2_frame = Frame(root, width=250, height=150)
q2_frame.grid(row=2, column=0, padx=5, pady=5, sticky="wens")

q3_frame = Frame(root, width=250, height=150)
q3_frame.grid(row=3, column=0, padx=5, pady=5, sticky="wens")

# titles

Label(title_frame, text="Please answer the following\n(from 1-5):").grid(row=1, column=0, padx=5)
Label(q1_frame, text="How much did you enjoy \n the recommended location?").grid(row=1, column=0, padx=5)
Label(q2_frame, text="Would you come back again??").grid(row=1, column=0, padx=5)
Label(q3_frame, text="Would you recommend to a friend?").grid(row=1, column=0, padx=5)

# questions
q1_slider = Scale(q1_frame, from_=0, to=5, orient="horizontal")
q1_slider.grid(row=2, column=0, padx=5)
logaction(" User answered first question@" + str(startdatetime))

q2_slider = Scale(q2_frame, from_=0, to=5, orient="horizontal")
q2_slider.grid(row=2, column=0, padx=5)
logaction(" User answered second question@" + str(startdatetime))

q3_slider = Scale(q3_frame, from_=0, to=5, orient="horizontal")
q3_slider.grid(row=2, column=0, padx=5)
logaction(" User answered third question@" + str(startdatetime))

# get the values from the sliders
q1_value = q1_slider.get()
q2_value = q2_slider.get()
q3_value = q3_slider.get()


import subprocess

def run_program():
    subprocess.call(["python", "Rbubbles"])


btn = Button(root, text='Next', command=run_program)
btn.grid()
logaction(" User has readjusted their suggestions@" + str(startdatetime))

root.mainloop()
