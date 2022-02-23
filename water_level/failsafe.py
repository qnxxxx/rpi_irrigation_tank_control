import RPi.GPIO as GPIO

from asgiref.sync import sync_to_async
from water_level.get_sonar_settings import FAILSAFE_PIN


@sync_to_async
def failsafe_status():
    if GPIO.input(FAILSAFE_PIN):
        print('NO FAILSAFE!')
        return False
    else:
        print('FAILSAFE!')
        # GPIO.cleanup(FAILSAFE_PIN)
        return True


# Get the Raspberry Pi mode status(BCM - 11 or BOARD - 10)
mode = GPIO.getmode()
if mode != 11:
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

GPIO.setup(FAILSAFE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
