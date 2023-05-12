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
# root.maxsize(900, 800)
root.config(bg="darkgreen")

left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

tool_bar = Frame(left_frame, width=180, height=185, bg="cyan")
tool_bar.grid(row=2, column=0, padx=5, pady=5)

right_frame = Frame(root, width=650, height=400, bg="orange")
right_frame.grid(row=0, column=1, padx=10, pady=5)

Label(left_frame, text="Logo").grid(row=1, column=0, padx=5)


def setcursor(x):
    right_frame.config(cursor=x)
    logaction("setcursor: " + x)


Button(tool_bar, text="cursor_dot", command=lambda: setcursor("dot")).grid(row=2, column=1, padx=6, pady=6, sticky="wens")
Button(tool_bar, text="cursor_normal", command=lambda: setcursor("arrow")).grid(row=3, column=1, padx=6, pady=6, sticky="wens")
# user_in = input("Type anything you want ")
#
# Button(tool_bar, text="Crop", command=lambda: print(len(user_in))).grid(row=3, column=1, padx=6, pady=6, sticky="wens")

""""""""" Figure out how to do menus in GUI for tkinter python """""""""

# Button(tool_bar, text="Settings", command=lambda: Menu())


# image = PhotoImage(file="test.png")
# original_image = image.subsample(3,4)
# Label(left_frame, image=original_image).grid(row=1, column=0, padx=9)

Label(tool_bar, text="Tools", relief=SUNKEN).grid(row=0, column=1, padx=5)
Label(tool_bar, text="Filters", relief=RAISED).grid(row=1, column=1, padx=6)

Label(tool_bar, text="Select").grid(row=0, column=0, padx=5, pady=5)

Label(tool_bar, text="Rotate & Flip").grid(row=2, column=0, padx=5, pady=5)
Label(tool_bar, text="Resize").grid(row=3, column=0, padx=5, pady=5)
Label(tool_bar, text="Exposure").grid(row=4, column=0, padx=5, pady=5)

# new window (try to make this accessible only from the main frame, therefore this must be a child frame)

root = Tk()

languages = Button(root, text="language selection", command=root.quit)
languages.pack()
password = Button(root, text="reset password")
password.pack()
profile_pic = Button(root, text="change profile pic")
profile_pic.pack()


exit = Button(root, text="Exit", command=root.quit)
exit.pack()


""" Make sure to install the packages for clearing (was not included with Homebrew)"""
# clearing.bind("<Enter>", clear)

root.mainloop()
