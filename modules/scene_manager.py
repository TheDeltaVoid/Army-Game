from modules.menus import MainMenu

class SceneManager:
    def __init__(self):
        self.current = "main_menu"
        
        self.scenes = {
            "main_menu" : MainMenu()
        }

    def update(self, delta_time):
        if self.current == "main_menu":
            self.scenes[self.current].update(delta_time)

    def render(self):
        if self.current == "main_menu":
            self.scenes[self.current].render()
