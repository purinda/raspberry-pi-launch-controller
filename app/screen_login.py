from Tkinter import *
from widgets import StatusBar
import socket


class ScreenLogin():
    def __init__(self, master, q_visibility):
        master.title('Login')
        self.master = master
        self.q_visibility = q_visibility
        self.statusbar = StatusBar(self.master, bd=1, relief=SUNKEN, anchor=CENTER)
        self.statusbar.pack(side=BOTTOM, fill=X)

    def reload_timer(self):
        self.statusbar.set('Local IP: %s', socket.gethostbyname(socket.gethostname()))
        status = self.q_visibility.get()

        if status == 'SHOW':
            self.master.deiconify()
        elif status == 'HIDE':
            self.master.withdraw()

        # Call reload_timer after 1sec
        self.master.after(1000, self.reload_timer)

    def show(self):

        buttons_frame = Frame(self.master)
        buttons_frame.pack(side=TOP, fill=Y)

        btn_list = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', 'Clear', 'Login'
        ]

        # this also shows the calculator's button layout
        rel = 'ridge'

        # Draw the butons pad
        r = 1
        c = 0
        for b in btn_list:
            # partial takes care of function and argument
            Button(buttons_frame, text=b, width=5, height=2, relief=rel).grid(row=r, column=c)
            c += 1
            if c >= 3:
                c = 0
                r += 1

        pinentry_form = Frame(self.master)
        pinentry_form.pack(side=TOP, fill=BOTH)
        Entry(pinentry_form).pack(side=BOTTOM)

        self.reload_timer()
