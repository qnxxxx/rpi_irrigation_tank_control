from relay_control.models import RelayBoardPinout


# Reads settings for the relay board from db
def read_relay_board_settings():
    pump_pin, mains_pin, byp_pin = RelayBoardPinout.objects.query_all().values_list()[0][2:]
    return pump_pin, mains_pin, byp_pin


relay_board_pins = read_relay_board_settings()

# Trigger and echo GPIO pins for sonar
PUMP_PIN = relay_board_pins[0]
MAINS_PIN = relay_board_pins[1]

# Failsafe button (overflow) GPIO pin
BYP_PIN = relay_board_pins[2]
