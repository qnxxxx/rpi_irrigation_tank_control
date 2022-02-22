from tank_level.models import SampleMeasurementSettings


# Reads settings for the measurement
def read_measurement_settings():
    sample_size, sample_wait, temperature, measurements_interval = SampleMeasurementSettings.objects.query_all().values_list()[0][2:]
    return sample_size, float(sample_wait), temperature, measurements_interval


measurement_settings = read_measurement_settings()

# Trigger and echo GPIO pins for sonar
SAMPLE_SIZE = measurement_settings[0]
SAMPLE_WAIT = measurement_settings[1]
TEMPERATURE = measurement_settings[2]

# Failsafe button (overflow) GPIO pin
MEASUREMENTS_INTERVAL = measurement_settings[3]
