from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

import json

from .models import RelayBoardStatus
from .relay_board_operation import turn_pump_on, turn_pump_off, turn_mains_on, turn_mains_off, turn_byp_on, turn_byp_off, turn_all_on, turn_all_off


class RelayControlConsumer(AsyncJsonWebsocketConsumer):
    """
    Controls the relay board
    """

    async def connect(self):
        """
        Called on connection to accept the connection call:
        """
        print('RelayControlConsumer: connected ')
        await self.channel_layer.group_add('rc', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        print('RelayControlConsumer: disconnected')
        await self.channel_layer.group_discard('rc', self.channel_name)

    async def send_relay_board(self):
        """
        Sends the relay board status message to clients.
        """
        # Send the board status message
        data = await get_switch_states()
        for ele in data.items():
            payload = {}
            payload['switch'], payload['state'] = ele
            await self.send_json(payload)

    async def receive_json(self, content):
        """
         Receives the relay board status message from clients.
        """
        # Messages will have a "command" key we can switch on
        command = content.get('command')
        switch = content.get('switch')
        print(f'RelayBoardConsumer: receive_json: {str(command)}')
        if switch:
            print(switch)
        if command == 'turn_on':
            pass
        elif command == 'turn_off':
            pass
        elif command == 'get_relay_board_status':
            await self.send_relay_board()

    async def receive_wl(self):  # Possibly not necessary
        """
         Receives the water level message.
        """
        pass

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
def get_switch_states():
    payload = {}
    pump_state, mains_state, byp_state = RelayBoardStatus.objects.query_all().values_list()[0][2:]

    payload['pump'] = pump_state
    payload['mains'] = mains_state
    payload['byp'] = byp_state

    return payload
