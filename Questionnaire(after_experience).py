from tkinter import *
from datetime import datetime
import subprocess



def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("Started second questionnaire @" + str(startdatetime))

root = Tk()
root.geometry("300x500")
root.title("Questionnaire")

# set up the frames
title_frame = Frame(root, width=250, height=100)
title_frame.pack()

q1_frame = Frame(root, width=250, height=150)
q1_frame.pack()

q2_frame = Frame(root, width=250, height=150)
q2_frame.pack()

q3_frame = Frame(root, width=250, height=150)
q3_frame.pack()

# titles

Label(title_frame, text="Please answer the following\n(from 1-5):").pack()
Label(q1_frame, text="How much did you enjoy \n the recommended location?").pack()
Label(q2_frame, text="Would you come back again??").pack()
Label(q3_frame, text="Would you recommend to a friend?").pack()

# questions
q1_slider = Scale(q1_frame, from_=0, to=5, orient="horizontal")
q1_slider.pack()

q2_slider = Scale(q2_frame, from_=0, to=5, orient="horizontal")
q2_slider.pack()

q3_slider = Scale(q3_frame, from_=0, to=5, orient="horizontal")
q3_slider.pack()

def run_program():
    logaction(" User has readjusted their suggestions@" + str(datetime.now()))
    logaction(" first answer is: " + str(q1_slider.get()))
    logaction(" second answer is: " + str(q2_slider.get()))
    logaction(" third answer is: " + str(q2_slider.get()))
    root.destroy()
    subprocess.call(["python", "Rbubbles.py"])


btn = Button(root, text='Next', command=run_program)
btn.pack()

root.mainloop()
