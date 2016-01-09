#!/usr/bin/env python

# for python 3.x use 'tkinter' rather than 'Tkinter'
from Tkinter import Tk
from app.polling_thread import PollingThread
from app.screen_login import ScreenLogin
import Queue
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s', )

# Message passing queue for the OnOffThread
q_status = Queue.Queue()


def showLogin(root_window):
    login = ScreenLogin(root_window)
    login.show()

def main():
    myThread = PollingThread(q_status, logging)
    myThread.start()

    root_window = Tk()
    root_window.title('Phoenix Launch Controller')
    root_window.minsize(240, 320)
    root_window.maxsize(240, 320)
    showLogin(root_window)


if __name__ == '__main__':
    logging.debug(__name__)
    main()
