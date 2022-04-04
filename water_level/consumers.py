from django.utils import timezone
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
# Import some kind of scheduler

from asgiref.sync import asyncio
from water_level.models import WaterLevel
from water_level.measurement import Measurement
from helpers.rpi_gpio_init import board_init
from helpers.get_tank_size import TANK_LENGTH, TANK_WIDTH, TANK_DEPTH, TANK_CAPACITY
from helpers.get_measurements_interval import MEASUREMENT_INTERVAL
from helpers.timestamp import calculate_timestamp


# Example taken from:
# https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py
class WaterLevelConsumer(AsyncJsonWebsocketConsumer):
    """
    Pulls tank level data from db and sends it to level gauge and level history chart
    """

    async def connect(self):
        """
        Called on connection to accept the connection call:
        """
        print('WaterLevelConsumer: connected ')
        await self.accept()
        await self.take_measurement()

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        print('WaterLevelConsumer: disconnected')

    async def take_measurement(self):
        """
        Called automatically on regular intervals
        """
        if init_state:
            measurement = await Measurement()
            while True:
                current_measurement = await measurement.distance()

                if current_measurement['status'] == 'Success!' and 10 <= current_measurement['water_level'] < TANK_DEPTH:
                    water_level = current_measurement['water_level']
                    volume_m3 = round((TANK_LENGTH * TANK_WIDTH * water_level) / 1000000, 2)
                    volume_l = round(volume_m3 * 1000)
                    tank_fill = round((volume_m3 * 100) / TANK_CAPACITY, 2)
                    current_measurement['volume_m3'] = volume_m3
                    current_measurement['volume_l'] = volume_l
                    current_measurement['tank_fill'] = tank_fill

                    print(current_measurement)

                elif current_measurement['water_level'] < 10 or current_measurement['water_level'] >= TANK_DEPTH:
                    current_measurement['status'] = 'Error: Inaccurate measurement!'

                    print(current_measurement)

                timestamp = calculate_timestamp(timezone.localtime(timezone.now()))
                await self.send_json(
                    {
                        'water_level': current_measurement['water_level'],
                        'volume_m3': current_measurement['volume_m3'],
                        'volume_l': current_measurement['volume_l'],
                        'tank_fill': current_measurement['tank_fill'],
                        'status': current_measurement['status'],
                        'failsafe': current_measurement['failsafe'],
                        'natural_timestamp': timestamp,
                    },
                )

                await create_water_level_db_entry(**current_measurement)

                await asyncio.sleep(MEASUREMENT_INTERVAL)

        else:
            print(f'INIT ERROR: {init_message}')

    async def handle_client_error(self, e):
        """
        Called when a ClientError is raised.
        Sends error data to UI.
        """
        error_data = dict()
        error_data['error'] = e.code
        if e.message:
            error_data['message'] = e.message
            await self.send_json(error_data)


@database_sync_to_async
def create_water_level_db_entry(water_level, volume_m3, volume_l, tank_fill, status, failsafe):
    return WaterLevel.objects.create(
        water_level=water_level,
        volume_m3=volume_m3,
        volume_l=volume_l,
        tank_fill=tank_fill,
        status=status,
        failsafe=failsafe
    )


init = board_init()
init_state, init_message = init['init_state'], init['status_message']
