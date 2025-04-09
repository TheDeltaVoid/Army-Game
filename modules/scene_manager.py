from scenes import game, load_game, menus

class SceneManager:
    def __init__(self, current_player_prefs):
        self.current_scene = "main_menu"
        self.scenes_list = {
            "main_menu" : menus.MainMenu(self, current_player_prefs),
            "load_game" : load_game.LoadGame(self, current_player_prefs),
            "game" : None
        }
        self.game_ready = False

    def preload_game(self):
        self.scenes_list["game"] = game.Game()

        self.game_ready = True

    def update(self, delta_time):
        self.scenes_list[self.current_scene].update(delta_time)

    def render(self):
        self.scenes_list[self.current_scene].render()
