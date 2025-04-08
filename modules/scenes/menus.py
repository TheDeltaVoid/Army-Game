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
        print(text_size.x)
        text_pos = pyray.Vector2((pyray.get_render_width() // 2) - (text_size.x // 2), (text_size.y // 2))
        pyray.draw_text_ex(font_format_1452, get_text("TITLE"), text_pos, TITLE_FONT_SIZE, TITLE_SPACING, TITLE_COLOR)