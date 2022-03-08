from channels.db import database_sync_to_async

from asgiref.sync import asyncio

from helpers.rpi_gpio_init import board_init
from water_level.measurement import Measurement
from water_level.models import WaterLevel
from water_level.get_tank_size import TANK_LENGTH, TANK_WIDTH, TANK_DEPTH
from water_level.get_measurements_interval import MEASUREMENT_INTERVAL


async def take_measurement():
    init = board_init()
    init_state, init_message = init['init_state'], init['status_message']

    if init_state:
        measurement = Measurement()
        while True:
            current_measurement = measurement.distance()

            if current_measurement['status_message'] == 'Success!' and 10 <= current_measurement['water_level'] < TANK_DEPTH:
                water_level = current_measurement['water_level']
                volume_m3 = round((TANK_LENGTH * TANK_WIDTH * (TANK_DEPTH - water_level)) / 1000000, 2)
                volume_l = round(volume_m3 * 1000)
                current_measurement['volume_m3'] = volume_m3
                current_measurement['volume_l'] = volume_l

                print(current_measurement)
                await create_water_level_db_entry(**current_measurement)

            elif current_measurement['water_level'] < 10 or current_measurement['water_level'] >= TANK_DEPTH:
                current_measurement['status_message'] = 'Error: Inaccurate measurement!'

                print(current_measurement)
                await create_water_level_db_entry(**current_measurement)

            await asyncio.sleep(MEASUREMENT_INTERVAL)

    else:
        print(f'init problem: {init_message}')


@database_sync_to_async
def create_water_level_db_entry(water_level, volume_m3, volume_l, status_message, failsafe_status):
    return WaterLevel.objects.create(
        water_level=water_level,
        volume_m3=volume_m3,
        volume_l=volume_l,
        status_message=status_message,
        failsafe_status=failsafe_status
    )
