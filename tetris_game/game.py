import json
import pygame

from tetris_game.board import Board
from settings import (
    WIDTH,
    HEIGHT,
    WHITE,
    FPS,
    TETRIS_ICON,
    TITLE_TETRIS,
    HIGHSCORE_FILE,
)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_TETRIS)
        icon = pygame.image.load(TETRIS_ICON)
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.board = Board()
        self._load_game()

    def _load_game(self):
        self.score = 0
        self.running = True
        try:
            with open(HIGHSCORE_FILE, encoding='utf-8') as f:
                data = json.load(f)
                self.highscore = data.get('tetris', 0)
        except (FileNotFoundError, json.JSONDecodeError):
            self.highscore = 0

    def _save_highscore(self):
        if self.score <= self.highscore:
            return

        try:
            data = json.load(open(HIGHSCORE_FILE))
        except Exception:
            data = {}

        data['tetris'] = self.score
        with open(HIGHSCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                key = event.key
                shape = self.board.current.shape
                x = self.board.current.x
                y = self.board.current.y

                if key == pygame.K_LEFT:
                    offset = (x - 1, y)
                    if self.board.valid_position(shape, offset):
                        self.board.current.x -= 1
                elif key == pygame.K_RIGHT:
                    offset = (x + 1, y)
                    if self.board.valid_position(shape, offset):
                        self.board.current.x += 1
                elif key == pygame.K_UP:
                    rotated = self.board.current.rotate()
                    if self.board.valid_position(
                        rotated, (x, y)
                    ):
                        self.board.current.shape = rotated
                elif key == pygame.K_DOWN:
                    offset = (x, y + 1)
                    if self.board.valid_position(shape, offset):
                        self.board.current.y += 1

    def update(self):
        shape = self.board.current.shape
        x = self.board.current.x
        y = self.board.current.y + 1

        if not self.board.valid_position(shape, (x, y)):
            self.board.freeze()
            self.score += 10
        else:
            self.board.current.y += 1

    def draw_ui(self):
        font = pygame.font.SysFont(None, 24)
        text = f'Score: {self.score}  Highscore: {self.highscore}'
        label = font.render(text, True, WHITE)
        self.screen.blit(label, (10, 10))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.board.draw(self.screen)
            self.draw_ui()
            pygame.display.flip()
            self.clock.tick(FPS)

        self._save_highscore()
        pygame.quit()
