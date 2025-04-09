import pyray
import math
import modules.game_manager as game_manager

from constants.game import *

class Game:
    def __init__(self):
        self.gm = game_manager.GameManager()
        map_image = pyray.gen_image_perlin_noise(MAP_SIZE_X, MAP_SIZE_Y, 0, 0, 1)
        self.game_map = pyray.load_texture_from_image(map_image)
        pyray.unload_image(map_image)

    def start(self):
        pass

    def update(self, delta_time):
        if pyray.is_mouse_button_down(pyray.MOUSE_BUTTON_LEFT) :
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

    def render(self):
        pyray.clear_background(BG_COLOR)

        pyray.begin_mode_2d(self.gm.camera)

        pyray.draw_texture(self.game_map, -(MAP_SIZE_X // 2), -(MAP_SIZE_Y // 2), pyray.GREEN)

        pyray.rl_push_matrix()
        pyray.rl_translatef(0, 1250, 0)
        pyray.rl_rotatef(90, 1, 0, 0)
        pyray.draw_grid(50, 100)
        pyray.rl_pop_matrix()

        pyray.end_mode_2d()