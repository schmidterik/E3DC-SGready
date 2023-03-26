from time import sleep

from modbus import E3DC
from display import SGDisplay
from relay import SGRelay

e3dc = E3DC()
display = SGDisplay()
relay = SGRelay()

def main():
    pv = e3dc.get_photovoltaic_power()
    bat = e3dc.get_battery_power()
    house = e3dc.get_house_consumption()
    grid = e3dc.get_grid_transfer_power()
    soc = e3dc.get_battery_soc()

    

    display.update_battery_power(bat)
    display.update_house_power(house)
    display.update_grid_power(grid)
    display.update_solar_power(pv)


if __name__ == "__name__":
    try:
        main()
    except KeyboardInterrupt:
        relay.cleanup()
        display.stop()

while True:
    sleep(10)