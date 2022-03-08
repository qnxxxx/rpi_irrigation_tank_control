from water_level.models import TankSize


# Reads tank size from db
def read_tank_size():
    length, width, depth = TankSize.objects.query_all().values_list()[0][2:]
    return float(length), float(width), float(depth)


sizes = read_tank_size()

# Measurements of the tank
TANK_LENGTH = sizes[0]
TANK_WIDTH = sizes[1]
TANK_DEPTH = sizes[2]
