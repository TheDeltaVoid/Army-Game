import pyray

from constants.game import *

class UnitType:
    def __init__(self, speed, field_of_view, attack_range, min_height, max_height, image):
        self.speed = speed
        self.field_of_view = field_of_view
        self.attack_range = attack_range
        self.min_height = min_height
        self.max_height = max_height
        self.image = image

    def check_position(self, height):
        if (height < self.min_height) or (height > self.max_height):
            return False
        return True

    def can_move(self, distance, height):
        if (distance > self.speed) or not self.check_position(height):
            return False
        return True

class Unit:
    def __init__(self, unit_type, x, y, side_color):
        self.unit_type = unit_type
        image = pyray.load_image(unit_type.image)
        self.texture = pyray.load_texture_from_image(image)
        pyray.unload_image(image)

        self.x = x
        self.y = y

        self.side_color = side_color

    def move(self, x, y, distance, height):
        if (self.unit_type.can_move(distance, height)):
            self.x = x
            self.y = y

    def draw(self, screen_pos, selected = False, selectable = False):
        color = (self.side_color if not selectable else SELECTABLE_COLOR) if not selected else SELECTED_COLOR

        pyray.draw_texture(self.texture, int(screen_pos.x) - (UNIT_SIZE_X // 2),
                           int(screen_pos.y) - (UNIT_SIZE_X // 2),
                           color)
