#!/usr/bin/env python

from app.onoffthread import OnOffThread
from Tkinter import Tk
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s', )


def showLogin():
    root = Tk()
    root.title("")
    root.minsize(240, 320)
    root.mainloop()


if __name__ == '__main__':
    myThread = OnOffThread()
    myThread.start()

    showLogin()