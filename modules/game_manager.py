import pyray
import math
import random
import modules.text as text
import modules.unit as unit

from constants.unit_types import *
from constants.game import *

class GameManager:
    def __init__(self, current_player_prefs):
        self.current_player_prefs = current_player_prefs

        self.camera = pyray.Camera2D()
        self.camera.zoom = 1.0
        self.camera.offset = pyray.Vector2(pyray.get_render_width()//2, pyray.get_render_height()//2)

        self.game_map = map_utils.Map(MAP_SIZE_X, MAP_SIZE_Y)

        self.time = 0

        self.ally_units = []
        self.enemy_units = []
        self.all_units = []

        self.selected_unit = None

    def find_valid_position(self, unit_type):
        valid_pos = False
        x = 0
        y = 0
        while not valid_pos :
            x = random.randrange(0, MAP_SIZE_X - 1)
            y = random.randrange(0, MAP_SIZE_Y - 1)
            valid_pos = unit_type.check_position(self.game_map.height(pyray.Vector2(x, y)))
        return (x, y)

    def initial_place_unit(self):
        for unit_to_place in ARMY_COMPOSITION:
            x, y = self.find_valid_position(unit_to_place)
            new_unit = unit.Unit(unit_to_place, x, y, ALLY_COLOR)
            self.ally_units.append(new_unit)
            self.all_units.append(new_unit)
            x, y = self.find_valid_position(unit_to_place)
            new_unit = unit.Unit(unit_to_place, x, y, ENEMY_COLOR)
            self.enemy_units.append(new_unit)
            self.all_units.append(new_unit)

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

    def map_point_to_screen_point(self, pos):
        new_position = pyray.get_world_to_screen_2d(pyray.Vector2(pos.x, pos.y), self.camera)

        new_position = pyray.vector2_add(new_position, pyray.Vector2(1, 1))

        return new_position


    def select_unit(self, pos):
        pos = self.screen_point_to_map_point(pos)
        min_distance = math.inf
        best_unit = None

        for unit_to_check in self.ally_units:
            unit_pos = pyray.Vector2(unit_to_check.x, unit_to_check.y)
            distance = pyray.vector2_distance(unit_pos, pos)
            if distance < min_distance:
                best_unit = unit_to_check
                min_distance = distance

        if min_distance > SELECT_DISTANCE:
            self.selected_unit = None
        else :
            self.selected_unit = best_unit

    def draw_units(self):
        for single_unit in self.ally_units:
            single_unit.draw(self.map_point_to_screen_point(pyray.Vector2(single_unit.x, single_unit.y)), single_unit == self.selected_unit)
        for single_unit in self.enemy_units:
            single_unit.draw(self.map_point_to_screen_point(pyray.Vector2(single_unit.x, single_unit.y)))

    def calc_infos(self, mouse_position):
        selected_point = pyray.Vector2(self.selected_unit.x, self.selected_unit.y)
        mouse_position_map = self.screen_point_to_map_point(mouse_position)
        mouse_distance = self.game_map.dist(selected_point, mouse_position_map)

        return (selected_point, mouse_distance, mouse_position_map)

    def render_info(self, mouse_position, secondary_font, main_font):
        selected_point = pyray.Vector2(0, 0)
        mouse_distance = 0
        mouse_position_map = pyray.Vector2(0, 0)

        if self.selected_unit != None :
            selected_point, mouse_distance, mouse_position_map = self.calc_infos(mouse_position)

        mouse_position_text = f"({int(mouse_position_map.x)};{int(mouse_position_map.y)})" + (f" <-> {int(mouse_distance) / 10}km" if self.selected_unit != None else "")

        pyray.draw_circle_v(mouse_position,
                            MOUSE_POS_CIRCLE_SIZE,
                            MOUSE_POS_CIRCLE_COLOR)
        if self.selected_unit != None :
            pyray.draw_line_v(mouse_position,
                              self.map_point_to_screen_point(selected_point),
                              LINE_COLOR)
        pyray.draw_text_ex(secondary_font,
                           mouse_position_text,
                           pyray.vector2_add(
                               mouse_position,
                               MOUSE_POS_TEXT_POSITION),
                           MOUSE_POS_TEXT_FONT_SIZE,
                           MOUSE_POS_TEXT_SPACING,
                           MOUSE_POS_TEXT_COLOR)

        time_text = text.get_text("TIME", self.current_player_prefs) + str(self.time)
        time_text_size = pyray.measure_text_ex(main_font, time_text, TIME_TEXT_FONT_SIZE, TIME_TEXT_SPACING)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (time_text_size.x // 2), (time_text_size.y // 2))
        pyray.draw_text_ex(main_font,
                           time_text,
                           text_pos,
                           TIME_TEXT_FONT_SIZE,
                           TIME_TEXT_SPACING,
                           TIME_TEXT_COLOR)
