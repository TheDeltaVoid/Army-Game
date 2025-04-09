import pyray

class GameManager:
    def __init__(self):
        self.camera = pyray.Camera2D()
        self.camera.zoom = 1.0
        self.camera.offset = pyray.Vector2(pyray.get_render_width()//2, pyray.get_render_height()//2)