from scenes import game, load_screen, menus

class SceneManager:
    def __init__(self, current_player_prefs):
        self.current_scene = "main_menu"
        self.scenes_list = {
            "main_menu" : None,
            "load_screen" : None,
            "game" : None
        }
        self.scene_ready = False
        self.current_player_prefs = current_player_prefs

    def change_scene(self, scene_id, next_scene_id = ""):
        if self.scenes_list[scene_id] == None:
            self.load_scene(scene_id, next_scene_id)

        self.current_scene = scene_id
        self.scenes_list[self.current_scene].start()

    def load_scene(self, scene_id, next_scene_id=""):
        match scene_id:
            case "game":
                self.scenes_list["game"] = game.Game()
            case "main_menu":
                self.scenes_list["main_menu"] = menus.MainMenu(self, self.current_player_prefs)
            case "load_screen":
                self.scenes_list["load_screen"] = load_screen.LoadScreen(self, self.current_player_prefs, next_scene_id)

        self.scene_ready = True

    def update(self, delta_time):
        try :
            self.scenes_list[self.current_scene].update(delta_time)
        except AttributeError:
            self.load_scene("main_menu")
            self.change_scene("main_menu")

    def render(self):
        try :
            self.scenes_list[self.current_scene].render()
        except AttributeError:
            self.load_scene("main_menu")
            self.change_scene("main_menu")