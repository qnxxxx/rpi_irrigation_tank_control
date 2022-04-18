import RPi.GPIO as GPIO

from helpers.get_sonar_settings import TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN
from helpers.get_relay_board_settings import PUMP_PIN, MAINS_PIN, BYP_PIN


def sonar_rpi_gpio_soft_cleanup():
    # Only cleanup the pins used by the sonar to prevent clobbering any others in use by the program
    print('Cleaning up the RPi GPIO pins used by the sonar!')
    GPIO.cleanup((TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN))


def relay_board_rpi_gpio_soft_cleanup():
    # Only cleanup the pins used by the relay board to prevent clobbering any others in use by the program
    print('Cleaning up the RPi GPIO pins used by the relay board!')
    GPIO.cleanup((PUMP_PIN, MAINS_PIN, BYP_PIN))
