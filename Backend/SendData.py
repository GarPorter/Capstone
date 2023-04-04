from Backend.SvgToPoints import *
import time
import asyncio
from bleak import BleakClient

DEVICE_ADDRESS = "00:11:22:33:44:55" # MAC address of Raspberry Pi Bluetooth Adapter
SERVICE_UUID = "00000000-0000-0000-0000-000000000001" # Use BLE scanner on rpi to find
CHARACTERISTIC_UUID = "00000000-0000-0000-0000-000000000002" # Use BLE scanner on rpi to find

def getPoints(fileName):
    points = svg_to_points(fileName, 2)[2:-6]
    # asyncio.run(send_data(points))


# async def send_data(data):
#     async with BleakClient(DEVICE_ADDRESS) as client:
#         await client.connect()
#         await client.write_gatt_char(CHARACTERISTIC_UUID, data.encode("utf-8"))
#         await client.disconnect()
