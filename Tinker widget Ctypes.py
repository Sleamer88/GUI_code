import tkinter as tk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.geometry("200x150")

label = tk.Label(root, text="Hello World")
label.pack(padx=5, pady=5)

root.mainloop()