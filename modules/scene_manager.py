from scenes.menus import MainMenu
from scenes.game import Game

class SceneManager:
    def __init__(self, current_player_prefs):
        self.current_scene = "main_menu"
        self.scenes = {
            "main_menu" : MainMenu(self, current_player_prefs),
            "game" : Game()
        }

    def update(self, delta_time):
        self.scenes[self.current_scene].update(delta_time)

    def render(self):
        self.scenes[self.current_scene].render()
