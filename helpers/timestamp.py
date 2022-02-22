from datetime import datetime

from django.contrib.humanize.templatetags.humanize import naturalday


def calculate_timestamp(timestamp):
    """
    1. Today or yesterday:
        - EX: 'today at 22:56:00'
        - EX: 'yesterday at 15:19'
    2. other:
        - EX: 25/06/2020
        - EX: 28/12/2020
    """
    # Today or yesterday
    if (naturalday(timestamp) == 'today') or (naturalday(timestamp) == 'yesterday'):
        str_time = datetime.strftime(timestamp, '%H:%M:%S')
        ts = f'{naturalday(timestamp)} at {str_time}'
    # Other days
    else:
        str_time = datetime.strftime(timestamp, '%d/%m/%Y')
        ts = f'{str_time}'
    return str(ts)
