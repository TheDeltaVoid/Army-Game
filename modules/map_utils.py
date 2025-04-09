import pyray
import random
import math

from constants.map_utils import *

class Map :
    def __init__(self, size_x, size_y):
        self.size_x, self.size_y = size_x, size_y

        map_image = pyray.gen_image_perlin_noise(size_x, size_y, random.randint(0, OFFSET), random.randint(0, OFFSET), SCALE)
        self.map_table = []

        for y in range(size_y):
            for x in range(size_x):
                self.map_table.append(pyray.get_image_color(map_image, x, y).r * MAX_HEIGHT / 255)
        for i in range(256):
            pyray.image_color_replace(map_image, pyray.Color(i, i, i, 255), TERRAIN_TYPE(i * MAX_HEIGHT / 255))

        self.texture_map = pyray.load_texture_from_image(map_image)
        pyray.unload_image(map_image)

    def height(self, x, y):
        return self.map_table[y * self.size_x + x]

    def dist(self, x1, y1, x2, y2):
        h_dist_sq = math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)
        v_dist_sq = math.pow(self.height(x1, y1) - self.height(x2, y2), 2)

        return math.sqrt(h_dist_sq + v_dist_sq)

    def draw(self):
        pyray.draw_texture(self.texture_map, 0, 0, pyray.WHITE)
