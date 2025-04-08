from pyray import *

from modules.constants import *
from modules.scene_manager import SceneManager

def main():
    init_window(WIDTH, HEIGHT, TITLE)
    toggle_fullscreen()

    scene_manager = SceneManager()

    delta_time = 0

    while not window_should_close():
        delta_time = get_frame_time()

        scene_manager.update(delta_time)

        begin_drawing()
        clear_background(BLACK)

        scene_manager.render()

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()
