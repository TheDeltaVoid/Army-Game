import pyray
import modules.scene_manager as scene_manager
import modules.text as text

from constants.general import *
from constants.load_game import *

class LoadGame:
    def __init__(self, current_scene_manager, current_player_prefs):
        self.current_scene_manager = current_scene_manager
        self.current_player_prefs = current_player_prefs

        #self.current_scene_manager.preload_game()

    def update(self, delta_time):
        if self.current_scene_manager.game_ready :
            self.current_scene_manager.current_scene = "game"

    def render(self):
        background_image = pyray.load_image(BG_IMAGE)
        pyray.image_resize_nn(background_image, pyray.get_render_width(), pyray.get_render_height())
        background_texture = pyray.load_texture_from_image(background_image)
        pyray.unload_image(background_image)
        pyray.draw_texture(background_texture, 0, 0, pyray.WHITE)
        pyray.clear_background(pyray.BLANK)

        main_font = pyray.load_font_ex(MAIN_FONT, LOAD_TEXT_FONT_SIZE, None, 0)
        
        text_size = pyray.measure_text_ex(main_font, text.get_text("TITLE", self.current_player_prefs), LOAD_TEXT_FONT_SIZE, LOAD_TEXT_SPACING)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2),
                            (pyray.get_render_height() // 2) - (text_size.y // 2))
        pyray.draw_text_ex(main_font, text.get_text("LOAD", self.current_player_prefs), text_pos, LOAD_TEXT_FONT_SIZE, LOAD_TEXT_SPACING, LOAD_TEXT_COLOR)