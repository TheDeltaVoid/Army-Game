from pyray import *

from modules.menu.main import MainMenu

class SceneManager:
    def __init__(self):
        self.current = "menu"
        self.current_menu = "main"
        
        self.menus = {
            "main" : MainMenu()
        }

    def update(self, delta_time):
        if self.current == "menu":
            self.menus[self.current_menu].update(delta_time)

    def render(self):
        if self.current == "menu":
            self.menus[self.current_menu].render()
