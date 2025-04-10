import pyray
import math

from constants.game import *

class GameManager:
    def __init__(self):
        self.camera = pyray.Camera2D()
        self.camera.zoom = 1.0
        self.camera.offset = pyray.Vector2(pyray.get_render_width()//2, pyray.get_render_height()//2)

        self.game_map = map_utils.Map(MAP_SIZE_X, MAP_SIZE_Y)

    def move_view(self, delta):
        delta = pyray.vector2_scale(delta, -1.0/self.camera.zoom)
        self.camera.target = pyray.vector2_add(self.camera.target, delta)

    def zoom(self, mouse_position, wheel):
        mouse_world_pos = pyray.get_screen_to_world_2d(mouse_position, self.camera);
        self.camera.offset = mouse_position
        self.camera.target = mouse_world_pos
        scale = 0.2*wheel
        self.camera.zoom = pyray.clamp(math.exp(math.log(self.camera.zoom)+scale), MIN_ZOOM, MAX_ZOOM)
