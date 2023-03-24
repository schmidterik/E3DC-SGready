import threading
from time import sleep

from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

class SGDisplay:
    
    def __init__(self):
        self.update = False
        self.grid_power = None
        self.house_power = None
        self.battery_power = None
        self.solar_power = None
        self.sg_status = None

        serial = i2c(port=1, address=0x3C)
        self.device = sh1106(serial)
    
    def update_grid_power(self, power):
        self.grid_power = int(power)
    
    def update_house_power(self, power):
        self.house_power = int(power)

    def update_battery_power(self, power):
        self.battery_power = int(power)

    def update_solar_power(self, power):
        self.solar_power = int(power)

    def update_sg_status(self, status):
        self.sg_status = int(status)

    def start(self):
        self.update = True
        thread = threading.Thread(target=self.update_display, daemon=False)
        thread.start()

    def stop(self):
        self.update = False

    def update_display(self):
        while self.update is True:
            print("Display aktualisiert")
            self._display()
            sleep(1)


    def _display(self):
        font2 = ImageFont.truetype('LiberationMono-Regular.ttf', 14)

        with canvas(self.device) as draw:
            if type(self.grid_power) == int:
                draw.text((0, 0),  f"Netz: {self.grid_power : >8} W", font=font2, fill="white")
            else:
                draw.text((0, 0),  f"Netz:       n.a.", font=font2, fill="white")
            
            if type(self.battery_power) == int:
                draw.text((0, 12), f"Batterie: {self.battery_power : >4} W", font=font2, fill="white")
            else:
                draw.text((0, 12), f"Batterie:   n.a.", font=font2, fill="white")
            
            if type(self.solar_power) == int:
                draw.text((0, 26), f"Solar: {self.solar_power : >7} W", font=font2, fill="white")
            else:
                draw.text((0, 26), f"Solar:      n.a.", font=font2, fill="white")

            if type(self.house_power) == int:
                draw.text((0, 38), f"Haus: {self.house_power : >8} W", font=font2, fill="white")
            else:
                draw.text((0, 38), f"Haus:       n.a.", font=font2, fill="white")

            if type(self.sg_status) == int:
                draw.text((0, 50), f"SG-Status: {self.sg_status : >3}  ", font=font2, fill="white")
            else:
                draw.text((0, 50), f"SG-Status:  n.a.", font=font2, fill="white")

    