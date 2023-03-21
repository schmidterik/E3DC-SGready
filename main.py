from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from modbus import E3DC
from time import sleep

bucket = "smarthome"

client = InfluxDBClient(url="http://192.168.178.36:8086", token="H4fmGvCZnoFLyQ0l0snVvY9uMaVzYawJWXP9yUMqg2i6QlpuSjdpQgfUDWg7eJJpG4NhDCuHd27T_-USlw0vpg==", org="Schmidt-Neuenstein")
write_api = client.write_api(write_options=SYNCHRONOUS)
e3dc = E3DC()

while True:
    p = Point("E3DC").field("photovoltaic_power", e3dc.get_photovoltaic_power())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("battery_power", e3dc.get_battery_power())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("house_consumption", e3dc.get_house_consumption())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("grid_transfer_power", e3dc.get_grid_transfer_power())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("additional_feeders_power", e3dc.get_additional_feeders_power())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("wallbox_power", e3dc.get_wallbox_power())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("wallbox_solarpower", e3dc.get_wallbox_solarpower())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("autarky", e3dc.get_autarky())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("self_consumption", e3dc.get_self_consumption())
    write_api.write(bucket=bucket, record=p)
    p = Point("E3DC").field("battery_soc", e3dc.get_battery_soc())
    write_api.write(bucket=bucket, record=p)
    sleep(10)
