import pyray
import math
import modules.map_utils as map_utils
import modules.game_manager as game_manager

from constants.general import *
from constants.game import *

class Game:
    def __init__(self, current_player_prefs):
        self.secondary_font = pyray.load_font_ex(SECONDARY_FONT, MOUSE_POS_TEXT_FONT_SIZE, None, 0)
        self.main_font = pyray.load_font_ex(MAIN_FONT, TIME_TEXT_FONT_SIZE, None, 0)
        self.gm = game_manager.GameManager(current_player_prefs)

        self.current_mouse_position = pyray.Vector2(0, 0)

    def start(self):
        self.gm.initial_place_unit()

    def update(self, delta_time):
        self.current_mouse_position = pyray.get_mouse_position()

        if pyray.is_mouse_button_down(pyray.MOUSE_BUTTON_LEFT):
            self.gm.move_view(pyray.get_mouse_delta())

        wheel = pyray.get_mouse_wheel_move()
        if wheel != 0:
            self.gm.zoom(self.current_mouse_position, wheel)

        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_RIGHT):
            self.gm.select_unit(self.current_mouse_position)

    def render(self):
        pyray.clear_background(BG_COLOR)

        self.gm.draw_map()

        self.gm.draw_units(self.current_mouse_position)

        self.gm.draw_fog_of_war()

        self.gm.render_info(self.current_mouse_position, self.secondary_font, self.main_font)
