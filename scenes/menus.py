import pyray

from modules.constants.general import *
from modules.constants.menu import *
from modules.text import *

class MainMenu:
    def __init__(self):
        pass

    def update(self, delta_time):
        pass

    def render(self):
        pyray.clear_background(BG_COLOR)

        font_format_1452 = pyray.load_font_ex(FONT_FORMAT_1452, TITLE_FONT_SIZE, None, 0)
        
        text_size = pyray.measure_text_ex(font_format_1452, get_text("TITLE"), TITLE_FONT_SIZE, TITLE_SPACING)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2), (text_size.y // 2))
        pyray.draw_text_ex(font_format_1452, get_text("TITLE"), text_pos, TITLE_FONT_SIZE, TITLE_SPACING, TITLE_COLOR)


        button_text_size = pyray.measure_text_ex(font_format_1452, get_text("PLAY"), PLAY_BUTTON_TEXT_FONT_SIZE, PLAY_BUTTON_TEXT_SPACING)
        button_size = pyray.Vector2(button_text_size.x + (PLAY_BUTTON_PADDING * 2), button_text_size.y + (PLAY_BUTTON_PADDING * 2))
        button_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2) - PLAY_BUTTON_PADDING,
                            (pyray.get_render_height() // 2) - (text_size.y // 2) - PLAY_BUTTON_PADDING)
        button_text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2),
                            (pyray.get_render_height() // 2) - (text_size.y // 2))
        pyray.draw_rectangle_v(button_pos, button_size, PLAY_BUTTON_COLOR)
        pyray.draw_text_ex(font_format_1452, get_text("PLAY"), button_text_pos, PLAY_BUTTON_TEXT_FONT_SIZE, PLAY_BUTTON_TEXT_SPACING, PLAY_BUTTON_TEXT_COLOR)
