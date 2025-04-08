import pyray

from modules.constants import *
from modules.text import *

class MainMenu:
    def __init__(self):
        pass

    def update(self, delta_time):
        pass

    def render(self):
        pyray.draw_text(get_text("TITLE"), 0, 0, TITLE_FONT_SIZE, TITLE_COLOR)