import pyray
import modules.scene_manager as scene_manager

from constants.general import *

def main():
    pyray.init_window(WIDTH, HEIGHT, TITLE)
    pyray.toggle_fullscreen()

    current_scene_manager = scene_manager.SceneManager()

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
