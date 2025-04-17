import json
import pygame

from settings import (
    WIDTH,
    HEIGHT,
    BLACK,
    WHITE,
    FPS,
    SNAKE_ICON,
    HIGHSCORE_FILE,
    TITLE_SNAKE,
)
from snake_game.snake import Snake
from snake_game.food import Food


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_SNAKE)
        icon = pygame.image.load(SNAKE_ICON)
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self._load_game()

    def _load_game(self):
        self.snake = Snake((WIDTH // 2, HEIGHT // 2))
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.running = True
        try:
            with open(HIGHSCORE_FILE, encoding='utf-8') as f:
                data = json.load(f)
                self.highscore = data.get('snake', 0)
        except (FileNotFoundError, json.JSONDecodeError):
            self.highscore = 0

    def _save_highscore(self):
        if self.score <= self.highscore:
            return

        try:
            data = {}
            if open(HIGHSCORE_FILE):
                data = json.load(open(HIGHSCORE_FILE))
        except Exception:
            data = {}

        data['snake'] = self.score
        with open(HIGHSCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)
                if event.key == pygame.K_r and self.game_over:
                    self._load_game()

    def update(self):
        if self.game_over:
            return

        self.snake.move()

        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food = Food()

        head_x, head_y = self.snake.body[0]
        collision = (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
            or self.snake.body[0] in self.snake.body[1:]
        )
        if collision:
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self._draw_ui()

        if self.game_over:
            self._draw_game_over()

        pygame.display.flip()

    def _draw_ui(self):
        font = pygame.font.SysFont(None, 24)
        text = f'Score: {self.score}  Highscore: {self.highscore}'
        label = font.render(text, True, WHITE)
        self.screen.blit(label, (10, 10))

    def _draw_game_over(self):
        font = pygame.font.SysFont(None, 48)
        text = 'Game Over! Press R to restart'
        label = font.render(text, True, WHITE)
        rect = label.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(label, rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        self._save_highscore()
        pygame.quit()
