import pyray

from modules.constants import *
from modules.scene_manager import SceneManager

def main():
    pyray.init_window(WIDTH, HEIGHT, TITLE)
    pyray.toggle_fullscreen()

    scene_manager = SceneManager()

    delta_time = 0

    while not pyray.window_should_close():
        delta_time = pyray.get_frame_time()

        scene_manager.update(delta_time)

        pyray.begin_drawing()
        pyray.clear_background(BG_COLOR)

        scene_manager.render()

        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
