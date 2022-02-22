from tank_level.models import TankSize


# Reads tank size from db
def read_tank_size():
    length, width, depth = TankSize.objects.query_all().values_list()[0][2:]
    return float(length), float(width), float(depth)


sizes = read_tank_size()

# Real size of the tank
LENGTH = sizes[0]
WIDTH = sizes[1]
DEPTH = sizes[2]
