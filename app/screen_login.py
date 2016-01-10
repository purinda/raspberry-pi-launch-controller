from Tkinter import *
from widgets import StatusBar


class ScreenLogin:
    def __init__(self, master, q_visibility):
        master.title('Login')
        self.master = master
        self.statusbar = 0
        self.q_visibility = q_visibility

    def reload_timer(self):
        self.statusbar.set('Current IP %s', 'XXX.XXX.XXX.XXX')
        status = self.q_visibility.get()

        if status == 'SHOW':
            self.master.deiconify()
        elif status == 'HIDE':
            self.master.withdraw()

        # Call reload_timer after 1sec
        self.master.after(1000, self.reload_timer)

    def show(self):
        self.statusbar = StatusBar(self.master)
        self.statusbar.pack(side=BOTTOM, fill=X)
        self.reload_timer()

        self.master.mainloop()
