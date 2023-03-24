import RPi.GPIO as GPIO

class SGRelay:

    def __init__(self):
        # pin definition
        self.SG_relay1_pin = 23
        self.SG_relay2_pin = 22
        self.ADD_relay1_pin = 24
        self.ADD_relay2_pin = 27

        # state variables
        self.sg_status = 0
        self.SG_relay1_state = False
        self.SG_relay2_state = False
        self.ADD_relay1_state = False
        self.ADD_relay2_state = False

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)

        # turn off all relays
        chan_list = (22,23,24,27)
        GPIO.output(chan_list, True)

    def set_SG_status(self, status):
        if status == 1:
            # Betriebszustand: Sperrung
            self.SG_relay1_ON()
            self.SG_relay2_OFF()
        elif status == 2:
            # Betriebszustand: Normalbetrieb
            self.SG_relay1_OFF()
            self.SG_relay2_OFF()
        elif status == 3:
            # Betriebszustand: Verstärkter Betrieb
            self.SG_relay1_OFF()
            self.SG_relay2_ON()
        elif status == 4:
            # Betriebszustand: Anlauf
            self.SG_relay1_ON()
            self.SG_relay2_ON()

    def get_SG_status(self) -> int:
        return self.sg_status

    def ADD_relay1_OFF(self):
        self.ADD_relay1_state = False
        GPIO.output(self.ADD_relay1_pin, True)

    def ADD_relay1_ON(self):
        self.ADD_relay1_state = True
        GPIO.output(self.ADD_relay1_pin, False)

    def ADD_relay2_OFF(self):
        self.ADD_relay2_state = False
        GPIO.output(self.ADD_relay2_pin, True)
    
    def ADD_relay2_ON(self):
        self.ADD_relay2_state = True
        GPIO.output(self.ADD_relay2_pin, False)

    def SG_relay1_OFF(self):
        self.SG_relay1_state = False
        GPIO.output(self.SG_relay1_pin, True)
    
    def SG_relay1_ON(self):
        self.SG_relay1_state = True
        GPIO.output(self.SG_relay1_pin, False)

    def SG_relay2_OFF(self):
        self.SG_relay2_state = False
        GPIO.output(self.SG_relay2_pin, True)
    
    def SG_relay2_ON(self):
        self.SG_relay2_state = True
        GPIO.output(self.SG_relay2_pin, False)

if __name__ == "__main__":
    relay = SGRelay()
    relay.set_SG_status(3)
    GPIO.cleanup()
