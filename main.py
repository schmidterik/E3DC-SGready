from time import sleep

try:
    from luma.core.error import DeviceNotFoundError
    from modbus import E3DC
    from display import SGDisplay
    from relay import SGRelay
except ModuleNotFoundError:
    print("""The following packages are required:
    - luma.oled
    - pyModbusTCP
    - RPi.GPIO
To install all required packages, execute the following command:
    pip install luma.oled pyModbusTCP RPi.GPIO
    """)
    exit()


def close():
        # return to normal state and close application
        print("Closing...")
        relay.set_SG_status(2)
        relay.cleanup()
        display.stop()
        exit()

# global variables
e3dc = E3DC()
try:
    display = SGDisplay()
except DeviceNotFoundError:
    close()
relay = SGRelay()
sg_state = 2

def main():
    global sg_state
    # collect data from E3DC
    try:
        pv = e3dc.get_photovoltaic_power()
        bat = e3dc.get_battery_power()
        house = e3dc.get_house_consumption()
        grid = e3dc.get_grid_transfer_power()
        soc = e3dc.get_battery_soc()
    except TypeError:
        print("ERROR: E3DC no connection")
        close()

    # If currently SG_status is 2 (normal operation),
    #  then check if SG_status should be changed to 3
    if sg_state == 2:
        # calculate sg state
        sg_state = 3
        # battery state of charge must be above 95%
        if soc <= 95:
            sg_state = 2
        # Self-consumption must be below 80%
        if float(house)/pv > 0.8:
            sg_state = 2
        # Grid feed-in must be greater than or equal to 1000 watts
        if grid >= -1000:
            sg_state = 2
    
    # If currently SG_status is 3, 
    # then check if SG_status should be changed to 2.
    elif sg_state == 3:
        sg_state = 2

        # battery discard above 50 watts
        if bat >= -50:
            sg_state = 3
        # state of charge below 95%
        if soc >= 95:
            sg_state = 3
        # power from grid above 200 watts
        if grid <= 200:
            sg_state = 3
    
    relay.set_SG_status(sg_state)

    # update display
    try:
        display.update_battery_power(bat)
        display.update_house_power(house)
        display.update_grid_power(grid)
        display.update_solar_power(pv)
        display.update_sg_status(sg_state)
    except DeviceNotFoundError:
        print("ERROR: display not working")
        close()

if __name__ == "__main__":
    print("Starting E3DC-SGready application...")
    try:
        while True:
            main()
            sleep(60)
    except KeyboardInterrupt:
        close()