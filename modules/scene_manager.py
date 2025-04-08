from modules.scenes.menus import MainMenu

current_scene = "main_menu"

class SceneManager:
    def __init__(self):        
        self.scenes = {
            "main_menu" : MainMenu()
        }

    def update(self, delta_time):
        self.scenes[current_scene].update(delta_time)

    def render(self):
        self.scenes[current_scene].render()
