import pyray
import modules.scene_manager as scene_manager
import modules.player_prefs as player_prefs

from constants.general import *

def main():
    current_player_prefs = player_prefs.PlayerPrefs()
    pyray.init_window(current_player_prefs.width, current_player_prefs.height, TITLE)
    pyray.toggle_fullscreen()

    current_scene_manager = scene_manager.SceneManager(current_player_prefs)

    delta_time = 0

    while not pyray.window_should_close():
        delta_time = pyray.get_frame_time()

        current_scene_manager.update(delta_time)

        pyray.begin_drawing()

        current_scene_manager.render()

        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
