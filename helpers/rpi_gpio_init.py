try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Probably because you need superuser privileges. Use 'sudo' to run your script.")

from water_level.get_sonar_settings import TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN
from relay_control.get_relay_board_settings import PUMP_PIN, MAINS_PIN, BYP_PIN


def board_init():
    # Make sure rpi mode is set to BCM
    try:
        if GPIO.getmode() is None:
            GPIO.setmode(GPIO.BCM)

        elif GPIO.getmode() != 11:
            GPIO.cleanup()
            GPIO.setmode(GPIO.BCM)

        # GPIO.setwarnings(False)  # Uncomment to hide RPi GPIO warnings in console
        # setup input/output pins
        # Sonar
        GPIO.setup(TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)
        GPIO.setup(FAILSAFE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # Relays
        GPIO.setup(PUMP_PIN, GPIO.OUT)
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        GPIO.setup(MAINS_PIN, GPIO.OUT)
        GPIO.output(MAINS_PIN, GPIO.HIGH)
        GPIO.setup(BYP_PIN, GPIO.OUT)
        GPIO.output(BYP_PIN, GPIO.HIGH)
        init_status = 'Success!'
        return {'init_state': True, 'status_message': init_status}

    except Exception as e:
        init_status = f'Board initialization failed! Error: {e}.'
        GPIO.cleanup()
        return {'init_state': False, 'status_message': init_status}
