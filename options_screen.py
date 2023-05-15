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
root.title("Reccomendations")

root.geometry("300x500")

#category title
category = Canvas(root,width=300, height=100)
category.grid(row=0, rowspan= 2, sticky="n")
o_category = category.create_oval(2,2,298,48)
t_category = category.create_text(148,23, text="Party/Clubbing")


root.mainloop()