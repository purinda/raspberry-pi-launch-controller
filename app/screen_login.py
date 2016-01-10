# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from widgets import StatusBar
from functools import partial
import socket
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s', )


class ScreenLogin(Tk):
    def __init__(self, master, q_visibility):
        master.title('Login')
        self.master = master
        self.pin_entry = None
        self.q_visibility = q_visibility
        self.statusbar = StatusBar(self.master, bd=1, relief=SUNKEN, anchor=CENTER)
        self.statusbar.pack(side=BOTTOM, fill=X)

    def refresh_timer(self):
        self.statusbar.set('Local IP: %s', socket.gethostbyname(socket.gethostname()))
        status = self.q_visibility.get()

        if status == 'SHOW':
            self.master.deiconify()
        elif status == 'HIDE':
            self.master.withdraw()

        # Call reload_timer after 1sec
        self.master.after(1000, self.refresh_timer)

    def process_key(self, key):
        logging.debug('Button Pressed: ' + key)

        if (key == 'Clear'):
            self.pin_entry.delete(0, END)
            return None

        if (key == 'Login'):
            if self.pin_entry.get() == '2117':
                tkMessageBox.showinfo(title="Welcome", message="Login successful, initiating launch system.")
            else:
                tkMessageBox.showwarning(title="Invalid attempt", message="Incorrect! please try again.")

            self.pin_entry.delete(0, END)
            return None

        self.pin_entry.insert(END, key)

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
        row = 1
        col = 0
        for b in btn_list:
            cmd = partial(self.process_key, b)

            # partial takes care of function and argument
            Button(buttons_frame, command=cmd, text=b,
                   width=5, height=2, relief=rel).grid(row=row, column=col)

            col += 1
            if col >= 3:
                col = 0
                row += 1

        pinentry_form = Frame(self.master)
        pinentry_form.pack(side=TOP, fill=BOTH)
        self.pin_entry = Entry(pinentry_form, show="•", font="Helvetica 24 bold", justify="center")
        self.pin_entry.pack(side=BOTTOM)

        self.refresh_timer()
