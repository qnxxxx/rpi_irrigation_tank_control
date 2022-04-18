from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

import json

from .models import AutomaticMode


class ModeConsumer(AsyncJsonWebsocketConsumer):
    """
    Controls mode of work: Auto/Manual
    """

    async def connect(self):
        """
        Called on connection to accept the connection call:
        """
        print('ModeConsumer: connected ')
        await self.channel_layer.group_add('mode', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        print('ModeConsumer: disconnected')
        await self.channel_layer.group_discard('mode', self.channel_name)

    async def send_mode_state(self):
        """
        Sends the mode switch state message to clients.
        """
        payload = await get_mode_state()

        await self.send_json(payload)

    async def receive_json(self, content):
        """
         Receives the mode switch status message from clients.
        """
        # Messages will have a "command" key we can switch on
        command = content.get('command', None)
        print(f'ModeConsumer: receive_json: {str(command)}')
        if command == 'auto':
            await set_mode_state(True)
            # await self.send_mode_state()
            print('Mode set to AUTO!')
        elif command == 'manual':
            await set_mode_state(False)
            # await self.send_mode_state()
            print('Mode set to MANUAL!')
        elif command == 'get_mode':
            await self.send_mode_state()

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
def get_mode_state():
    mode_state = AutomaticMode.objects.query_all().values_list()[0][-1]

    return mode_state


@database_sync_to_async
def set_mode_state(state):
    mode = AutomaticMode.objects.get(id=1)
    mode.automatic_mode_enabled = state
    mode.save()
