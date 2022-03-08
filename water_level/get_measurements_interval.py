from water_level.models import MeasurementsInterval


# Reads settings for the measurement
def read_measurement_interval():
    interval = MeasurementsInterval.objects.query_all().values_list()[0][2]
    return interval


MEASUREMENT_INTERVAL = read_measurement_interval()
