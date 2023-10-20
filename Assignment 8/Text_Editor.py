# This Program Creates a text editor with a horizontal and vertical scollbar

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Editor")
root.geometry("%dx%d+0+0" % root.maxsize())
root.state('zoomed')

text = tk.Text(root, wrap="none")
text.pack(expand=True, fill='both')

text.insert('1.0', "Type Here")

scrollbar = tk.Scrollbar(text, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y', anchor=tk.E)

text['yscrollcommand'] = scrollbar.set

scrollbar = tk.Scrollbar(text, orient='horizontal', command=text.xview)
scrollbar.pack(side='bottom', fill='x', anchor=tk.S)

text['xscrollcommand'] = scrollbar.set

root.mainloop()