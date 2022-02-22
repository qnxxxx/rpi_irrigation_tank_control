from tank_level.models import SonarPinout


# Reads settings for the sonar sensor from db
def read_sonar_settings():
    trigger_pin, echo_pin, failsafe_pin = SonarPinout.objects.query_all().values_list()[0][2:]
    return trigger_pin, echo_pin, failsafe_pin


sonar_pins = read_sonar_settings()

# Trigger and echo GPIO pins for sonar
TRIGGER_PIN = sonar_pins[0]
ECHO_PIN = sonar_pins[1]

# Failsafe button (overflow) GPIO pin
FAILSAFE_PIN = sonar_pins[2]
