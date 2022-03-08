from water_level.models import SampleMeasurement


# Reads settings for the measurement
def read_measurement_settings():
    sample_size, sample_wait, temperature = SampleMeasurement.objects.query_all().values_list()[0][2:]
    return sample_size, float(sample_wait), temperature


measurement_settings = read_measurement_settings()

SAMPLE_SIZE = measurement_settings[0]
SAMPLE_WAIT = measurement_settings[1]
TEMPERATURE = measurement_settings[2]
