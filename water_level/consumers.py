from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

import json

from water_level.models import WaterLevel


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
        await self.channel_layer.group_add('wl', self.channel_name)
        await self.accept()
        last_lvl = await get_last_water_level()
        await self.send_json(last_lvl)

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        print('WaterLevelConsumer: disconnected')
        await self.channel_layer.group_discard('wl', self.channel_name)

    async def send_wl(self, event):
        """
        Sends the water level to clients.
        """
        text_message = event['water_level']

        await self.send_json(text_message)

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
def get_last_water_level():
    last_measurement = WaterLevel.objects.all().last()
    last_timestamp, last_water_level, last_vol_m3, last_vol_l, last_tank_fill, last_failsafe, last_status = str(last_measurement).split(', ')
    payload = {
        'water_level': last_water_level,
        'volume_m3': last_vol_m3,
        'volume_l': last_vol_l,
        'tank_fill': last_tank_fill,
        'status': last_status,
        'failsafe': last_failsafe,
        'natural_timestamp': 'last db record'
    }

    return payload
