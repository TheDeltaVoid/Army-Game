import pyray

OFFSET = 10000
SCALE = 3

DEFAULT_PRECISION=5

MAX_HEIGHT = 100

def TERRAIN_TYPE(value):
    if 0 <= value <= 10:
        return pyray.Color(0, 105, 148, 255)# WATER
    elif 10 <= value <= 20:
        return pyray.Color(45, 137, 239, 255)# WATER
    elif 20 <= value <= 30:
        return pyray.Color(95, 158, 160, 255)# WATER
    elif 30 <= value <= 40:
        return pyray.Color(119, 255, 57, 255)# FIELD
    elif 40 <= value <= 50:
        return pyray.Color(69, 186, 12, 255)# FIELD
    elif 50 <= value <= 60:
        return pyray.Color(0, 166, 16, 255)# FIELD
    elif 60 <= value <= 70:
        return pyray.Color(9, 107, 0, 255)# FOREST
    elif 70 <= value <= 80:
        return pyray.Color(173, 88, 28, 255)# MOUNTAIN
    elif 80 <= value <= 90:
        return pyray.Color(139, 69, 19, 255)# MOUNTAIN
    elif 90 <= value <= 100:
        return pyray.Color(101, 67, 33, 255)# MOUNTAIN
    else :
        return pyray.Color(255, 0, 255, 255)
