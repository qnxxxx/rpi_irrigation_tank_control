try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! Probably because you need superuser privileges. Use 'sudo' to run your script.")

from helpers.get_sonar_settings import TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN
from relay_control.get_relay_board_settings import PUMP_PIN, MAINS_PIN, BYP_PIN


def rpi_gpio_soft_cleanup():
    # Only cleanup the pins used to prevent clobbering any others in use by the program??
    GPIO.cleanup((TRIGGER_PIN, ECHO_PIN, FAILSAFE_PIN, PUMP_PIN, MAINS_PIN, BYP_PIN))
