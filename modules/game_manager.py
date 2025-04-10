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

    def screen_point_to_map_point(self, pos):
        new_position = pyray.get_screen_to_world_2d(pyray.Vector2(pos.x - 1, pos.y - 1), self.camera)

        new_position = pyray.vector2_clamp(new_position, pyray.Vector2(0, 0), pyray.Vector2(self.game_map.size_x - 1, self.game_map.size_y - 1))

        return new_position

