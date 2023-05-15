# from tkinter import *
# from datetime import datetime
#
# def logaction(logtext):
#     delta = datetime.now() - startdatetime
#     logfile.write(str(delta) + "" + logtext + "\n")
#
#
# startdatetime = datetime.now()
# starttime = datetime.timestamp(startdatetime)
# logfile = open("logging_prototype.txt", "a")
# logaction("New user tracking session @" + str(startdatetime))
#
# root = Tk()
# root.title("Welcome")
#
#
# #Define the geometry of window
# root.geometry("1000x4000")
#
# #Create a canvas object
# c= Canvas(root,width=400, height=400)
# c.pack()
#
# #Draw an Oval in the canvas
# c.create_oval(60,60,210,210)
#
# #Create a canvas object
# c= Canvas(root,width=400, height=400)
# c.pack()
#
# #Draw an Oval in the canvas
# c.create_oval(61,61,209,209)
#
# root.mainloop()

# import math
# import tkinter as tk
#
# def draw(angle, text):
#     x = math.cos(math.radians(angle)) * 50 + 250
#     y = math.sin(math.radians(angle)) * 50 + 250
#     obj = canvas.create_text(250, 250, text=text, fill="green")
#     canvas.itemconfig(obj, angle=-angle)
#     canvas.coords(obj, x, y)
#     return obj
#
# root = tk.Tk()
# canvas = tk.Canvas(root, width=500, height=500)
#
# for i in range(0,360,60):
#     draw(i,"Hi")
#
# canvas.pack()
# root.mainloop()