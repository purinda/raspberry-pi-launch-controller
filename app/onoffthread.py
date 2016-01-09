import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

class OnOffThread(threading.Thread):
    """
    This thread will keep a checking the On/Off status of the main switch.
    If
        - On:  The GUI of the launcher will be shown.
        - Off: The GUI of the launcher will be hidden.
    """

    def __init__(self):
        threading.Thread.__init__(self)
        threading.Thread.name = 'OnOff Interrupt'
        self.counter = 0

    def run(self):
        while True:
            time.sleep(1)
            self.counter += 1
            logging.debug("Polling GPIO interrupt (" + str(self.counter) + ')')
