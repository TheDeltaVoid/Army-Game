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

class Unit:
    def __init__(self, unit_type, x, y, side_color):
        self.unit_type = unit_type
        image = pyray.load_image(unit_type.image)
        self.texture = pyray.load_texture_from_image(image)
        pyray.unload_image(image)

        self.x = x
        self.y = y

        self.side_color = side_color

    def can_move(self, distance, height):
        if (distance > self.unit_type.speed) or (height < self.unit_type.min_height) or (height > self.unit_type.max_height):
            return False
        return True

    def move(self, x, y, distance, height):
        if (self.can_move(distance, height)):
            self.x = x
            self.y = y

    def draw(self, screen_pos):
        pyray.draw_texture(self.texture, int(screen_pos.x) - (UNIT_SIZE_X // 2), int(screen_pos.y) - (UNIT_SIZE_X // 2), self.side_color)
