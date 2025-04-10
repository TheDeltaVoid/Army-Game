import pyray

OFFSET = 10000
SCALE = 3

DEFAULT_PRECISION=5

MAX_HEIGHT = 100

def TERRAIN_TYPE(value):
    if 0 <= value <= 10:
        return pyray.Color(0, 105, 148, 255)
    elif 10 <= value <= 20:
        return pyray.Color(45, 137, 239, 255)
    elif 20 <= value <= 30:
        return pyray.Color(95, 158, 160, 255)
    elif 30 <= value <= 40:
        return pyray.Color(34, 139, 34, 255)
    elif 40 <= value <= 50:
        return pyray.Color(107, 142, 35, 255)
    elif 50 <= value <= 60:
        return pyray.Color(128, 141, 38, 255)
    elif 60 <= value <= 70:
        return pyray.Color(156, 129, 58, 255)
    elif 70 <= value <= 80:
        return pyray.Color(141, 92, 68, 255)
    elif 80 <= value <= 90:
        return pyray.Color(139, 69, 19, 255)
    elif 90 <= value <= 100:
        return pyray.Color(101, 67, 33, 255)
    else :
        return pyray.Color(255, 0, 255, 255)
