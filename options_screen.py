from tkinter import *
from tkinter import ttk
from datetime import datetime
from PIL import Image,ImageTk

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
category = Canvas(root,width=300, height=50)
category.grid(row=0, columnspan= 2, sticky="n")
o_category = category.create_oval(2,2,298,48)
t_category = category.create_text(148,23, text="Party/Clubbing")

Label(root, text="Results for clubs in Amsterdam:").grid(row=1, columnspan=2)

import subprocess

def run_program():
    subprocess.call(["python", "Info_page.py"])


btn = Button(root, text='Next', command=run_program)
btn.grid()

#club Jimmy woo
jim = ImageTk.PhotoImage(Image.open("./Images/jimmy.png").resize((140,100)))

jim_frame = Frame(root, width=300, height= 150, bg="lightgrey")
jim_frame.grid(row=2, column=0, columnspan=2, pady=4)

Label(jim_frame, text="Jimmy Woo").grid(row=0, column=0,columnspan=2, pady=4)
Label(jim_frame, image=jim).grid(row=1, column=0)
Label(jim_frame, text="Exclusive nightclub with an elegant Asian-style bar and a dance floor with more than 12,000 lights.", wraplength=140).grid(row=1, column=1)

#club Escape
escape = ImageTk.PhotoImage(Image.open("./Images/escape.png").resize((140,100)))

escape_frame = Frame(root, width=300, height= 150, bg="lightgrey")
escape_frame.grid(row=3, column=0, columnspan=2, pady=4)

Label(escape_frame, text="Escape").grid(row=0, column=0, columnspan=2, pady=4)
Label(escape_frame, image=escape).grid(row=1, column=0)
Label(escape_frame, text="Vibrant nightclub with a dance floor, DJs, a VIP area and a well-stocked bar.", wraplength=140).grid(row=1, column=1)

#club Air
air = ImageTk.PhotoImage(Image.open("./Images/air.png").resize((140,100)))

air_frame = Frame(root, width=300, height= 150, bg="lightgrey")
air_frame.grid(row=4, column=0, columnspan=2, pady=4)

Button(air_frame, text="air", command= run_program).grid(row=0, column=0, columnspan=2, pady=4)
Label(air_frame, image=air).grid(row=1, column=0)
Label(air_frame, text="Huge club playing progressive dance music on multiple floors with 5 quirky bars.", wraplength=140).grid(row=1, column=1)
root.mainloop()
