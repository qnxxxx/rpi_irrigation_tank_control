import RPi.GPIO as GPIO

from relay_control.models import RelayBoardStatus
from helpers.get_relay_board_settings import PUMP_PIN, MAINS_PIN, BYP_PIN


def turn_pump_on():
    pump_pin_state = read_relay_board_status()[0]
    if not pump_pin_state:
        GPIO.output(PUMP_PIN, GPIO.LOW)
        relay_board.pump_pin_state = True
        relay_board.save()
        print('Pump: ON')
    else:
        print('Pump: ALREADY ON')


def turn_pump_off():
    pump_pin_state = read_relay_board_status()[0]
    if pump_pin_state:
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        relay_board.pump_pin_state = False
        relay_board.save()
        print('Pump: OFF')
    else:
        print('Pump: ALREADY OFF')


def turn_mains_on():
    mains_pin_state = read_relay_board_status()[1]
    if not mains_pin_state:
        GPIO.output(MAINS_PIN, GPIO.LOW)
        relay_board.mains_pin_state = True
        relay_board.save()
        print('Mains: ON')
    else:
        print('Mains: ALREADY ON')


def turn_mains_off():
    mains_pin_state = read_relay_board_status()[1]
    if mains_pin_state:
        GPIO.output(MAINS_PIN, GPIO.HIGH)
        relay_board.mains_pin_state = False
        relay_board.save()
        print('Mains: OFF')
    else:
        print('Mains: ALREADY OFF')


def turn_byp_on():
    byp_pin_state = read_relay_board_status()[2]
    if not byp_pin_state:
        GPIO.output(BYP_PIN, GPIO.LOW)
        relay_board.byp_pin_state = True
        relay_board.save()
        print('Bypass: ON')
    else:
        print('Bypass: ALREADY ON')


def turn_byp_off():
    byp_pin_state = read_relay_board_status()[2]
    if byp_pin_state:
        GPIO.output(BYP_PIN, GPIO.HIGH)
        relay_board.byp_pin_state = False
        relay_board.save()
        print('Bypass: OFF')
    else:
        print('Bypass: ALREADY OFF')


def turn_all_on():
    turn_pump_on()
    turn_mains_on()
    turn_byp_on()


def turn_all_off():
    turn_pump_off()
    turn_mains_off()
    turn_byp_off()


def read_relay_board_status():
    pump_pin_state, mains_pin_state, byp_pin_state = RelayBoardStatus.objects.query_all().values_list()[0][2:]
    return pump_pin_state, mains_pin_state, byp_pin_state


relay_board = RelayBoardStatus.objects.get(id=1)
