from scenes.menus import MainMenu
from scenes.game import Game

current_scene = "main_menu"

class SceneManager:
    def __init__(self):        
        self.scenes = {
            "main_menu" : MainMenu(),
            "game" : Game()
        }

    def update(self, delta_time):
        self.scenes[current_scene].update(delta_time)

    def render(self):
        self.scenes[current_scene].render()
