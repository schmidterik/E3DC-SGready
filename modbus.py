from pyModbusTCP.client import ModbusClient
from time import sleep


def _combine16bit(result):
    """
    This method combines tw0 16bit Integer from a list ([0] is L and [1] is H)
    and generates a 32bit signed Int.
    :param result:
    :return: 32bit signed int
    """
    value = (result[1] << 16) | (result[0])
    if (value >> 31) == 1:
        value = ~(0xFFFFFFFF - value)
    return value


class E3DC:
    def __init__(self):
        try:
            self.c = ModbusClient(host='192.168.178.65', port=502)
        except ValueError:
            print("Error with host or port params")

    def get_photovoltaic_power(self):
        """
        The function returns the current power production of the photovoltaic system.
        :return: photovoltaic
        """
        result = self.c.read_holding_registers(40067, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_battery_power(self):
        """
        The function returns the current power of the battery. Negative values mean a discharge.
        :return: battery power in Watt
        """
        result = self.c.read_holding_registers(40069, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_house_consumption(self):
        """

        :return: house consumption in Watt
        """
        result = self.c.read_holding_registers(40071, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_grid_transfer_power(self):
        """
        The function returns the current Power at grid transfer point. Negative values mean feeding into the power grid.
        :return: Power at grid transfer point in Watt
        """
        result = self.c.read_holding_registers(40073, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_additional_feeders_power(self):
        """
        The function returns the power of all additional feeders.
        :return: Power of all additional feeders in Watt
        """
        result = self.c.read_holding_registers(40075, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_wallbox_power(self):
        """

        :return:
        """
        result = self.c.read_holding_registers(40077, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_wallbox_solarpower(self):
        """

        :return:
        """
        result = self.c.read_holding_registers(40079, reg_nb=2)
        try:
            return _combine16bit(result)
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_autarky(self):
        """

        :return: autarky in percent
        """
        result = self.c.read_holding_registers(40081, reg_nb=1)
        try:
            return result[0] >> 8
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_self_consumption(self):
        """

        :return: self-consumption in percent
        """
        result = self.c.read_holding_registers(40081, reg_nb=1)
        try:
            return result[0] & 0x00FF
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

    def get_battery_soc(self):
        """
        The function returns the Battery state of charge in percent
        :return:
        """
        result = self.c.read_holding_registers(40082, reg_nb=1)
        try:
            return result[0]
        except TypeError:
            print("Data could not be retrieved from E3DC")
            raise

if __name__ == "__main__":
    e3dc = E3DC()

    print(f"Photovoltaik-Leistung: {e3dc.get_photovoltaic_power()} W")
    print(f"Batterie-Leistung: {e3dc.get_battery_power()} W")
    print(f"Hausverbraus-Leistung {e3dc.get_house_consumption()} W")
    print(f"Leistung am Netzübergabepunkt {e3dc.get_grid_transfer_power()} W")
    print(f"Leistung zusätzlicher Einspeiser: {e3dc.get_additional_feeders_power()} W")
    print(f"Leistung Wallbox: {e3dc.get_wallbox_power()} W")
    print(f"Solarleistung Wallbox: {e3dc.get_wallbox_solarpower()} W")
    print(f"Autarkie: {e3dc.get_autarky()} %")
    print(f"Eigenverbrauch: {e3dc.get_self_consumption()} %")
    print(f"Batterie-SOC: {e3dc.get_battery_soc()} %")
    print("")