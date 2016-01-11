#!/usr/bin/env python

# for python 3.x use 'tkinter' rather than 'Tkinter'
from Tkinter import Tk
from app.polling_thread import PollingThread
from app.screen_login import ScreenLogin
import Queue
import RPi.GPIO as GPIO
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s', )

# Message passing queue for the polling thread
q_visibility = Queue.Queue()


def showLogin(root_window):
    login = ScreenLogin(root_window, q_visibility)
    login.show()

def main():
    myThread = PollingThread(q_visibility, logging)
    myThread.start()

    root_window = Tk()
    root_window.title('Phoenix Launch Controller')
    root_window.minsize(240, 300)
    root_window.maxsize(240, 300)
    showLogin(root_window)
    root_window.mainloop()


if __name__ == '__main__':
    logging.debug(__name__)
    try:
        main()  
    except KeyboardInterrupt:
        logging.debug('Cleaning up GPIO registers...')

        GPIO.setmode(GPIO.BOARD)
        GPIO.cleanup()

