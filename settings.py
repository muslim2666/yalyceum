import os


WIDTH = 640
HEIGHT = 480
FPS = 10

TITLE_SNAKE = 'Snake Game'
TITLE_TETRIS = 'Tetris Game'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

CELL_SIZE = 20

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
HIGHSCORE_FILE = os.path.join(BASE_DIR, 'highscore.json')
SNAKE_ICON = os.path.join(ASSETS_DIR, 'snake_icon.png')
TETRIS_ICON = os.path.join(ASSETS_DIR, 'tetris_icon.png')