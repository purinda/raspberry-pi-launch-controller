import threading
import time
import RPi.GPIO as GPIO

# System On/Off GPIO (Board PIN)
PIN_ONOFF = 32
LED_ONLINE = 35

class PollingThread(threading.Thread):
    """
    This thread will keep a checking the On/Off status of the main switch.
    If
        - On:  The GUI of the launcher will be shown.
        - Off: The GUI of the launcher will be hidden.
    """

    def __init__(self, q_visibility, logging):
        threading.Thread.__init__(self)

        self.logging = logging
        self.timestamp = None
        self.gpio_value = None
        self.q_visibility = q_visibility
		
        # Setup GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN_ONOFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(LED_ONLINE, GPIO.OUT)

    def run(self):
        while True:
            time.sleep(1)
            self.gpio_value = GPIO.input(PIN_ONOFF)
            
            if self.gpio_value:
                self.q_visibility.put('HIDE')
                GPIO.output(LED_ONLINE, GPIO.LOW)
            else:
                self.q_visibility.put('SHOW')
                GPIO.output(LED_ONLINE, GPIO.HIGH)

            self.timestamp = time.time()
            self.logging.debug("GPIO Status [" + str(self.gpio_value) + '] @ ' + str(round(self.timestamp)))
