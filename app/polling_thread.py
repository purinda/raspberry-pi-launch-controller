import threading
import time

class PollingThread(threading.Thread):
    """
    This thread will keep a checking the On/Off status of the main switch.
    If
        - On:  The GUI of the launcher will be shown.
        - Off: The GUI of the launcher will be hidden.
    """

    def __init__(self, q_status, logging):
        threading.Thread.__init__(self)
        threading.Thread.name = 'OnOff Interrupt'

        self.logging = logging
        self.timestamp = 0
        self.gpio_value = 0
        self.q_status = q_status

    def run(self):
        while True:
            time.sleep(1)
            if round(self.timestamp) % 5:
                self.q_status.put(round(self.timestamp))

            self.timestamp = time.time()
            self.logging.debug("GPIO Status [" + str(self.gpio_value) + '] @ ' + str(round(self.timestamp)))