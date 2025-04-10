import pyray
import math
import modules.map_utils as map_utils
import modules.game_manager as game_manager

from constants.general import *
from constants.game import *

class Game:
    def __init__(self):
        self.secondary_font = pyray.load_font_ex(SECONDARY_FONT, MOUSE_POS_TEXT_FONT_SIZE, None, 0)
        self.gm = game_manager.GameManager()

        self.selected_point = pyray.Vector2(0, 0)
        self.current_mouse_distance = 0

    def start(self):
        pass

    def update(self, delta_time):
        if pyray.is_mouse_button_down(pyray.MOUSE_BUTTON_LEFT):
            self.gm.move_view(pyray.get_mouse_delta())

        wheel = pyray.get_mouse_wheel_move()
        if wheel != 0:
            self.gm.zoom(pyray.get_mouse_position(), wheel)

        current_mouse_position = self.gm.screen_point_to_map_point(pyray.get_mouse_position())

        self.current_mouse_distance = self.gm.game_map.dist(self.selected_point, current_mouse_position)

        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_RIGHT):
            self.selected_point = current_mouse_position

    def render(self):
        pyray.clear_background(BG_COLOR)

        pyray.begin_mode_2d(self.gm.camera)

        self.gm.game_map.draw()

        pyray.end_mode_2d()

        self.gm.render_info(pyray.get_mouse_position(), self.current_mouse_distance, self.selected_point, self.secondary_font)
