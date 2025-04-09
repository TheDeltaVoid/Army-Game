import pyray
import modules.scene_manager as scene_manager
import modules.text as text

from constants.general import *
from constants.menu import *

class MainMenu:
    def __init__(self):
        self.button_start_pos = pyray.Vector2(0,0)
        self.button_stop_pos = pyray.Vector2(0,0)

    def update(self, delta_time):
        if pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT) :
            mouse_pos = pyray.get_mouse_position()
            if mouse_pos.x > self.button_start_pos.x and mouse_pos.y > self.button_start_pos.y :
                if mouse_pos.x < self.button_stop_pos.x and mouse_pos.y < self.button_stop_pos.y :
                    scene_manager.current_scene = "game"

    def render(self):
        background_image = pyray.load_image(BG_IMAGE)
        pyray.image_resize_nn(background_image, pyray.get_render_width(), pyray.get_render_height())
        background_texture = pyray.load_texture_from_image(background_image)
        pyray.unload_image(background_image)
        pyray.draw_texture(background_texture, 0, 0, pyray.WHITE)
        pyray.clear_background(pyray.BLANK)

        main_font = pyray.load_font_ex(MAIN_FONT, TITLE_FONT_SIZE, None, 0)
        
        text_size = pyray.measure_text_ex(main_font, text.get_text("TITLE"), TITLE_FONT_SIZE, TITLE_SPACING)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2), (text_size.y // 2))
        pyray.draw_text_ex(main_font, text.get_text("TITLE"), text_pos, TITLE_FONT_SIZE, TITLE_SPACING, TITLE_COLOR)


        button_image = pyray.load_image(PLAY_BUTTON_IMAGE)

        button_text_size = pyray.measure_text_ex(main_font, text.get_text("PLAY"), PLAY_BUTTON_TEXT_FONT_SIZE, PLAY_BUTTON_TEXT_SPACING)
        button_size = pyray.Vector2(button_text_size.x + (PLAY_BUTTON_PADDING_X * 2), button_text_size.y + (PLAY_BUTTON_PADDING_Y * 2))
        
        button_text_pos = pyray.Vector2(PLAY_BUTTON_PADDING_X, PLAY_BUTTON_PADDING_Y)

        pyray.image_resize_nn(button_image, int(button_size.x), int(button_size.y))
        pyray.image_draw_text_ex(button_image, main_font, text.get_text("PLAY"), button_text_pos, PLAY_BUTTON_TEXT_FONT_SIZE, PLAY_BUTTON_TEXT_SPACING, PLAY_BUTTON_TEXT_COLOR)

        button_pos = pyray.Vector2((pyray.get_render_width() // 2) - (button_text_size.x // 2) - PLAY_BUTTON_PADDING_X,
                            (pyray.get_render_height() // 2) - (button_text_size.y // 2) - PLAY_BUTTON_PADDING_Y)
        
        button_texture = pyray.load_texture_from_image(button_image)
        pyray.unload_image(button_image)
        pyray.draw_texture_v(button_texture, button_pos, pyray.WHITE)

        self.button_start_pos = button_pos
        self.button_stop_pos = pyray.Vector2(button_pos.x + button_size.x,
                                            button_pos.y + button_size.y)