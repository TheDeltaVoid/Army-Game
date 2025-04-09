import pyray
import modules.scene_manager as scene_manager
import modules.text as text

from constants.general import *
from constants.load_screen import *

class LoadScreen:
    def __init__(self, current_scene_manager, current_player_prefs, scene_id):
        self.current_scene_manager = current_scene_manager
        self.current_player_prefs = current_player_prefs

        self.main_font = pyray.load_font_ex(MAIN_FONT, LOAD_TEXT_FONT_SIZE, None, 0)

        background_image = pyray.load_image(BG_IMAGE)
        pyray.image_resize_nn(background_image, pyray.get_render_width(), pyray.get_render_height())
        self.background_texture = pyray.load_texture_from_image(background_image)
        pyray.unload_image(background_image)

        self.scene_id = scene_id

    def start(self):
        pyray.begin_drawing()
        self.render()
        pyray.end_drawing()

        self.current_scene_manager.load_scene(self.scene_id)

    def update(self, delta_time):
        if self.current_scene_manager.scene_ready :
            self.current_scene_manager.current_scene = self.scene_id

    def render(self):
        pyray.draw_texture(self.background_texture, 0, 0, pyray.WHITE)
        pyray.clear_background(pyray.BLANK)
        
        text_size = pyray.measure_text_ex(self.main_font, text.get_text("TITLE", self.current_player_prefs), LOAD_TEXT_FONT_SIZE, LOAD_TEXT_SPACING)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2),
                            (pyray.get_render_height() // 2) - (text_size.y // 2))
        pyray.draw_text_ex(self.main_font, text.get_text("LOAD", self.current_player_prefs), text_pos, LOAD_TEXT_FONT_SIZE, LOAD_TEXT_SPACING, LOAD_TEXT_COLOR)