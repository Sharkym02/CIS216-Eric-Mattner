# This Program Creates a text editor with a horizontal and vertical scollbar
# This Program also has file and edit menus, which allow the user to create a new text, and/or exit the text editor
# The edit menu allows the user to cut, copy, and paste within the text editor

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Editor")
root.geometry("%dx%d+0+0" % root.maxsize())
root.state('zoomed')

text = tk.Text(root, wrap="none")
text.pack(expand=True, fill='both')

menuBar = tk.Menu(root)

clipboard = None

def cut():
    clipboard = text.selection_get()
    text.clipboard_clear()
    text.clipboard_append(clipboard)
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)


def copy():
    clipboard = text.selection_get()
    text.clipboard_clear()
    text.clipboard_append(clipboard)
    text.selection_clear

def paste():
    text.insert(tk.INSERT, text.selection_get(selection='CLIPBOARD'))

def reset():
    text.delete('1.0', tk.END)
    text.insert('1.0', "Type Here")


def PopupMenu(event):
    try:
        popupMenu.tk_popup(event.x_root, event.y_root, 0)        
    finally:
        popupMenu.grab_release()

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=reset)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = tk.Menu(menuBar, tearoff = 0)
editMenu.add_command(label="Cut (Ctrl+X)", command=cut)
editMenu.add_command(label="Copy (Ctrl+C)", command=copy)
editMenu.add_command(label="Paste (Ctrl+V)", command=paste)
menuBar.add_cascade(label="Edit", menu=editMenu)

popupMenu = tk.Menu(text, tearoff=0)
popupMenu.add_command(label="Cut (Ctrl+X)", command=cut)
popupMenu.add_command(label="Copy (Ctrl+C)", command=copy)
popupMenu.add_command(label="Paste (Ctrl+V)", command=paste)

text.bind("<Button-2>", PopupMenu)
text.bind("<Button-3>", PopupMenu)



text.insert('1.0', "Type Here")

scrollbar = tk.Scrollbar(text, orient='vertical', command=text.yview)
scrollbar.pack(side='right', fill='y', anchor=tk.E)

text['yscrollcommand'] = scrollbar.set

scrollbar = tk.Scrollbar(text, orient='horizontal', command=text.xview)
scrollbar.pack(side='bottom', fill='x', anchor=tk.S)

text['xscrollcommand'] = scrollbar.set

root.config(menu=menuBar)
root.mainloop()