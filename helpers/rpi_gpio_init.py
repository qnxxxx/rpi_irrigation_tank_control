try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Probably because you need superuser privileges. Use 'sudo' to run your script.")

from helpers.get_sonar_settings import TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN
from helpers.get_relay_board_settings import PUMP_PIN, MAINS_PIN, BYP_PIN
from core.models import BoardInitStatus


def board_init():
    print('Initializing RPi GPIO board...')
    # Make sure rpi mode is set to BCM
    try:
        if GPIO.getmode() is None:
            GPIO.setmode(GPIO.BCM)
            print('RPi GPIO board mode set to BCM')

        elif GPIO.getmode() != 11:
            print('RPi GPIO board is in wrong mode...')
            GPIO.cleanup()
            print('Switching mode...')
            GPIO.setmode(GPIO.BCM)
            print('RPi GPIO board mode set to BCM')

        # GPIO.setwarnings(False)  # Uncomment to hide RPi GPIO warnings in console

        # Setup input/output pins
        # Sonar
        print('Initializing sonar...')
        GPIO.setup(TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)
        GPIO.setup(FAILSAFE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('Sonar initialization complete!')

        # Relays
        print('Initializing relay board...')
        GPIO.setup(PUMP_PIN, GPIO.OUT)
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        GPIO.setup(MAINS_PIN, GPIO.OUT)
        GPIO.output(MAINS_PIN, GPIO.HIGH)
        GPIO.setup(BYP_PIN, GPIO.OUT)
        GPIO.output(BYP_PIN, GPIO.HIGH)
        print('Relay board initialization complete!')

        init_status = 'Success!'
        board.init_state = True
        board.save()
        return {'init_state': True, 'status_message': init_status}

    except Exception as e:
        init_status = f'Init Error: {e}.'
        GPIO.cleanup()
        board.init_state = False
        board.save()
        return {'init_state': False, 'status_message': init_status}


board = BoardInitStatus.objects.get(id=1)
