# This Program Creates a text editor with a horizontal and vertical scollbar
# This Program also has file, edit, and format menus
# The File menu allows the user to create a new text, open an existing text, save their current text, and exit the program
# The edit menu allows the user to cut, copy, and paste within the text editor
# The format menu allows the user to change the color of the text

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

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

def filePopup(text):
    messagebox.showinfo("File", text)

def open_file():
    select = filedialog.askopenfile(initialdir='/',
                                        title="Select a file", 
                                        filetypes=(('text files', '*.txt'),
                                        ('All files', '*.*'))
                                        )
    if select:
        text.delete('1.0', tk.END)
        text.insert('1.0', "".join(select.readlines()))

def save():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text.get("1.0", tk.END))
                filePopup("File Saved")
        except:
            filePopup("File Failed to Save")

def PopupMenu(event):
    try:
        popupMenu.tk_popup(event.x_root, event.y_root, 0)        
    finally:
        popupMenu.grab_release()

def choose_color():
    color = colorchooser.askcolor(title="Choose a color")
    # text.config(fg=color)
    text.config(foreground=color[1])
    root.update_idletasks

fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=reset)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save)
fileMenu.add_command(label="Save as", command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

editMenu = tk.Menu(menuBar, tearoff = 0)
editMenu.add_command(label="Cut (Ctrl+X)", command=cut)
editMenu.add_command(label="Copy (Ctrl+C)", command=copy)
editMenu.add_command(label="Paste (Ctrl+V)", command=paste)
menuBar.add_cascade(label="Edit", menu=editMenu)

formatMenu = tk.Menu(menuBar, tearoff=0)
formatMenu.add_command(label="Text Color", command=choose_color)
menuBar.add_cascade(label="Format", menu=formatMenu)

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