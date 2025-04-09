import pyray
import modules.scene_manager as scene_manager
import modules.text as text

from constants.general import *
from constants.menu import *

class MainMenu:
    def __init__(self, current_scene_manager, current_player_prefs):
        self.button_start_pos = pyray.Vector2(0,0)
        self.button_stop_pos = pyray.Vector2(0,0)

        self.current_scene_manager = current_scene_manager
        self.current_player_prefs = current_player_prefs

        self.main_font = pyray.load_font_ex(MAIN_FONT, TITLE_FONT_SIZE, None, 0)

        background_image = pyray.load_image(BG_IMAGE)
        pyray.image_resize_nn(background_image, pyray.get_render_width(), pyray.get_render_height())
        self.background_texture = pyray.load_texture_from_image(background_image)
        pyray.unload_image(background_image)

        button_image = pyray.load_image(PLAY_BUTTON_IMAGE)

        button_text_size = pyray.measure_text_ex(self.main_font, text.get_text("PLAY", self.current_player_prefs), PLAY_BUTTON_TEXT_FONT_SIZE, PLAY_BUTTON_TEXT_SPACING)
        self.button_size = pyray.Vector2(button_text_size.x + (PLAY_BUTTON_PADDING_X * 2), button_text_size.y + (PLAY_BUTTON_PADDING_Y * 2))
        
        button_text_pos = pyray.Vector2(PLAY_BUTTON_PADDING_X, PLAY_BUTTON_PADDING_Y)

        pyray.image_resize_nn(button_image, int(self.button_size.x), int(self.button_size.y))
        pyray.image_draw_text_ex(button_image, self.main_font, text.get_text("PLAY", self.current_player_prefs), button_text_pos, PLAY_BUTTON_TEXT_FONT_SIZE, PLAY_BUTTON_TEXT_SPACING, PLAY_BUTTON_TEXT_COLOR)

        self.button_pos = pyray.Vector2((pyray.get_render_width() // 2) - (button_text_size.x // 2) - PLAY_BUTTON_PADDING_X,
                            (pyray.get_render_height() // 2) - (button_text_size.y // 2) - PLAY_BUTTON_PADDING_Y)
        
        self.button_texture = pyray.load_texture_from_image(button_image)
        pyray.unload_image(button_image)

    def start(self):
        pass

    def update(self, delta_time):
        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT) :
            mouse_pos = pyray.get_mouse_position()
            if mouse_pos.x > self.button_start_pos.x and mouse_pos.y > self.button_start_pos.y :
                if mouse_pos.x < self.button_stop_pos.x and mouse_pos.y < self.button_stop_pos.y :
                    self.current_scene_manager.change_scene("load_screen", "game")

    def render(self):
        pyray.draw_texture(self.background_texture, 0, 0, pyray.WHITE)
        pyray.clear_background(pyray.BLANK)
        
        text_size = pyray.measure_text_ex(self.main_font, text.get_text("TITLE", self.current_player_prefs), TITLE_FONT_SIZE, TITLE_SPACING)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2), (text_size.y // 2))
        pyray.draw_text_ex(self.main_font, text.get_text("TITLE", self.current_player_prefs), text_pos, TITLE_FONT_SIZE, TITLE_SPACING, TITLE_COLOR)
        
        pyray.draw_texture_v(self.button_texture, self.button_pos, pyray.WHITE)

        self.button_start_pos = self.button_pos
        self.button_stop_pos = pyray.Vector2(self.button_pos.x + self.button_size.x,
                                            self.button_pos.y + self.button_size.y)