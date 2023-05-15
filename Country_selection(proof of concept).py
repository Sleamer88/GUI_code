from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

vlist = ["Netherlands"]
xlist = ["Amsterdam"]

Combov = ttk.Combobox(frame, values= vlist)
Combov.set("Choose a country")
Combov.pack(padx=5, pady=5)

Combox = ttk.Combobox(frame,values= xlist)
Combox.set("Choose a city")
Combox.pack(padx=6, pady=6)

# import subprocess
#
# def run_program():
#     subprocess.call(["python", "Account_overview.py"])
#
#
# btn = Button(root, text='Next', command=run_program)
# btn.pack()
#
# root.mainloop()
