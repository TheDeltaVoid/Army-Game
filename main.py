from pyray import *
from modules.constants import *

def main():
    init_window(WIDTH, HEIGHT, TITLE)

    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()
