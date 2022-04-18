from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# from core.models import BoardInitStatus
# from .relay_board_operation import turn_pump_on, turn_pump_off, turn_mains_on, turn_mains_off, turn_byp_on, turn_byp_off, turn_all_on, turn_all_off
#
# channel_layer = get_channel_layer()
#
#
# @shared_task
# def get_water_level():
#     if board_init_state:
#         water_level = Measurement().take_measurement()
#
#         async_to_sync(channel_layer.group_send)('wl', {'type': 'send_wl', 'water_level': water_level})
#
#
# board_init_state = BoardInitStatus.objects.query_all().values_list()[0][-1]
