import pyray
import math
import modules.map_utils as map_utils
import modules.game_manager as game_manager

from constants.game import *

class Game:
    def __init__(self):
        self.gm = game_manager.GameManager()

        self.game_map = map_utils.Map(MAP_SIZE_X, MAP_SIZE_Y)

        self.point_x = 0
        self.point_y = 0

    def start(self):
        pass

    def update(self, delta_time):
        if pyray.is_mouse_button_down(pyray.MOUSE_BUTTON_LEFT):
            delta = pyray.get_mouse_delta()
            delta = pyray.vector2_scale(delta, -1.0/self.gm.camera.zoom)
            self.gm.camera.target = pyray.vector2_add(self.gm.camera.target, delta)

        wheel = pyray.get_mouse_wheel_move()
        if wheel != 0:
            mouse_world_pos = pyray.get_screen_to_world_2d(pyray.get_mouse_position(), self.gm.camera);

            self.gm.camera.offset = pyray.get_mouse_position()

            self.gm.camera.target = mouse_world_pos

            scale = 0.2*wheel
            self.gm.camera.zoom = pyray.clamp(math.exp(math.log(self.gm.camera.zoom)+scale), 0.125, 4.0)

        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_RIGHT):
            print(self.game_map.dist(self.point_x, self.point_y, pyray.get_mouse_x(), pyray.get_mouse_y()))

            self.point_x = pyray.get_mouse_x()
            self.point_y = pyray.get_mouse_y()

    def render(self):
        pyray.clear_background(BG_COLOR)

        pyray.begin_mode_2d(self.gm.camera)

        self.game_map.draw()

        pyray.end_mode_2d()
