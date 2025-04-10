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

    def height(self, pos):
        return self.map_table[int(pos.y) * self.size_x + int(pos.x)]

    def dist(self, pos1, pos2, precision=DEFAULT_PRECISION):
        if precision < 2:
            h_dist_sq = pyray.vector2_distance_sqr(pos1, pos2)
            v_dist_sq = math.pow(self.height(pos1) - self.height(pos2), 2)
            return math.sqrt(h_dist_sq + v_dist_sq)

        xm = (pos1.x + pos2.x) // 2
        ym = (pos1.y + pos2.y) // 2
        middle = pyray.Vector2(xm, ym)

        return (self.dist(pos1, middle, precision-1) + self.dist(middle, pos2, precision-1))

    def draw(self):
        pyray.draw_texture(self.texture_map, 0, 0, pyray.WHITE)
