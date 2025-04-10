import pyray
import math
import modules.text as text

from constants.game import *

class GameManager:
    def __init__(self, current_player_prefs):
        self.current_player_prefs = current_player_prefs

        self.camera = pyray.Camera2D()
        self.camera.zoom = 1.0
        self.camera.offset = pyray.Vector2(pyray.get_render_width()//2, pyray.get_render_height()//2)

        self.game_map = map_utils.Map(MAP_SIZE_X, MAP_SIZE_Y)

        self.time = 0

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

    def render_info(self, mouse_position, mouse_distance, selected_point, secondary_font, main_font):
        mouse_position_map = self.screen_point_to_map_point(mouse_position)

        selected_point = self.map_point_to_screen_point(selected_point)

        mouse_position_text = f"({int(mouse_position_map.x)};{int(mouse_position_map.y)}) <-> {int(mouse_distance) / 10}km"

        pyray.draw_circle_v(mouse_position, MOUSE_POS_CIRCLE_SIZE, MOUSE_POS_CIRCLE_COLOR)
        pyray.draw_circle_v(selected_point, SELECTED_POS_CIRCLE_SIZE, SELECTED_POS_CIRCLE_COLOR)
        pyray.draw_line_v(mouse_position, selected_point, LINE_COLOR)
        pyray.draw_text_ex(secondary_font,
                           mouse_position_text,
                           pyray.vector2_add(mouse_position, MOUSE_POS_TEXT_POSITION),
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
