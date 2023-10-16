# This program creates a window that contains the text "Hello world!"

import tkinter

class Root(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title("Hello World")
        self.geometry("%dx%d+0+0" % self.maxsize())
        self.state('zoomed')

        label = tkinter.Label(
            text="Hello world!",
            width=320,
            height=240)
        label.pack()

if __name__ == "__main__":
    root = Root()
    root.mainloop()