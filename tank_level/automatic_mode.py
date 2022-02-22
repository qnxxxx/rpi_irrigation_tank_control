from django.utils import timezone

from asgiref.sync import asyncio

from helpers.timestamp import calculate_timestamp
from tank_level.measurement import Measurement
from tank_level.failsafe import failsafe_status
from tank_level.models import WaterLevel


async def measurement_db_entry():
    while True:
        current_measurement = Measurement().water_volume()
        print(current_measurement)
        if current_measurement:
            timestamp = calculate_timestamp(timezone.localtime(timezone.now()))
            print(f'{timestamp} : {current_measurement["water_level"]} cm : or {current_measurement["volume_m3"]} m3 : or {current_measurement["volume_l"]} liters.')

            WaterLevel.objects.create(
                distance=current_measurement['water_level'],
                volume_m3=current_measurement['volume_m3'],
                volume_l=current_measurement['volume_l'],
                status=current_measurement['status'],
                failsafe_engaged=failsafe_status
            )
        await asyncio.sleep(30)


failsafe_status = None

while True:
    failsafe_status = await failsafe_status()
    print(failsafe_status)
    await asyncio.sleep(3)

