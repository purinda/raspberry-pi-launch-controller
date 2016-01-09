from Tkinter import *
from widgets import StatusBar


class ScreenLogin:
    def __init__(self, master):
        master.title('Login')
        self.master = master

    def show(self):
        statusbar = StatusBar(self.master)
        statusbar.pack(side=BOTTOM, fill=X)

        statusbar.set('Current IP %s', '192.168.1.1')
        self.master.mainloop()
