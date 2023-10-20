# This program creates a window that contains the text "Hello world!"

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello World")
root.geometry("%dx%d+0+0" % root.maxsize())
root.state('zoomed')

text = tk.Text(root)
text.pack()

text.insert('1.0', "Hello World")

root.mainloop()