# from django.utils import timezone
# from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from channels.db import database_sync_to_async
# # Import some kind of scheduler
#
# import json
#
# from water_level.measurement import Measurement
# from water_level.models import SonarSettings, MeasurementSettings, TankLevel
# from chat.exceptions import ClientError
# from helpers.timestamp import calculate_timestamp
#
#
# # Example taken from:
# # https://github.com/andrewgodwin/channels-examples/blob/master/multichat/chat/consumers.py
# class TankLevelConsumer(AsyncJsonWebsocketConsumer):
#     """
#     Pulls tank level data from db and sends it to level gauge and level history chart
#     """
#     async def connect(self):
#         """
#         Called on connection to accept the connection call:
#         """
#         print('TankLevelConsumer: connected ')
#         await self.accept()
#
#     async def disconnect(self, code):
#         """
#         Called when the WebSocket closes for any reason.
#         """
#         # leave the room
#         print('TankLevelConsumer: disconnected')
#         try:
#             await self.leave_room(self.room_id)
#         except Exception as e:
#             print('EXCEPTION: ' + str(e))
#
#     async def auto_get_tank_level(self, event):
#         """
#         Called automatically on regular intervals
#         """
#         # Send a message down to the client
#         print('PublicChatConsumer: chat_message from user #' + str(event['user_id']))
#         timestamp = calculate_timestamp(timezone.now())
#         await self.send_json(
#             {
#                 'msg_type': MSG_TYPE_MESSAGE,
#                 'profile_image': event['profile_image'],
#                 'username': event['username'],
#                 'user_id': event['user_id'],
#                 'message': event['message'],
#                 'natural_timestamp': timestamp,
#             },
#         )
#
#     async def send_messages_payload(self, messages, new_page_number):
#         """
#         Send a payload of messages to the ui
#         """
#         print('PublicChatConsumer: send_messages_payload. ')
#
#         await self.send_json(
#             {
#                 'messages_payload': 'messages_payload',
#                 'messages': messages,
#                 'new_page_number': new_page_number,
#             },
#         )
#
#     async def handle_client_error(self, e):
#         """
#         Called when a ClientError is raised.
#         Sends error data to UI.
#         """
#         errorData = dict()
#         errorData['error'] = e.code
#         if e.message:
#             errorData['message'] = e.message
#             await self.send_json(errorData)
