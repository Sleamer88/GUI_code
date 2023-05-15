from tkinter import *
from datetime import datetime
import subprocess


def logaction(logtext):
    delta = datetime.now() - startdatetime
    logfile.write(str(delta) + "" + logtext + "\n")


startdatetime = datetime.now()
starttime = datetime.timestamp(startdatetime)
logfile = open("logging_prototype.txt", "a")
logaction("Questionnaire has been started @" + str(startdatetime))

root = Tk()
root.geometry("300x500")
root.title("Questionnaire")

# set up the frames
title_frame = Frame(root, width=300, height=100, pady=10)
title_frame.pack()

q1_frame = Frame(root, width=300, height=150)
q1_frame.pack()

q2_frame = Frame(root, width=300, height=150)
q2_frame.pack()

q3_frame = Frame(root, width=300, height=150)
q3_frame.pack()

# titles

Label(title_frame, text="Please answer the following:").pack()
Label(q1_frame, text="Do you like warm weather?").pack()
Label(q2_frame, text="Do you prefer cities over beaches?").pack()
Label(q3_frame, text="Do you like the historical aspects \n of a place?").pack()

# questions
q1_slider = Scale(q1_frame, from_=0, to=5, orient="horizontal")
q1_slider.pack()


q2_slider = Scale(q2_frame, from_=0, to=5, orient="horizontal")
q2_slider.pack()
logaction(" second question was answered@" + str(startdatetime))

q3_slider = Scale(q3_frame, from_=0, to=5, orient="horizontal")
q3_slider.pack()
logaction(" third question was answered@" + str(startdatetime))

def run_program():
    logaction(" User finished questionnaire@" + str(datetime.now()))
    logaction(" first answer is: " + str(q1_slider.get()))
    logaction(" second answer is: " + str(q2_slider.get()))
    logaction(" third answer is: " + str(q3_slider.get()))
    root.destroy()
    subprocess.call(["python", "Bubbles_page.py"])
    
    


btn = Button(root, text='Next', command=run_program)
btn.pack()
root.mainloop()
