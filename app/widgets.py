from Tkinter import *

class StatusBar(Frame):

    def __init__(self, master, **options):
        Frame.__init__(self, master)
        self.label = Label(self, **options)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()