import pyray

class MainMenu:
    def __init__(self):
        pass

    def update(self, delta_time):
        pass

    def render(self):
        pyray.draw_text("Hello, Window!", 0, 0, 20, WHITE)
        pyray.draw_text("In Main Menu", 0, 200, 20, WHITE)
