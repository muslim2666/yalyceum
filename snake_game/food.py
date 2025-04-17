import random
import pygame

from settings import CELL_SIZE, RED, WIDTH, HEIGHT


class Food:
    def __init__(self):
        self.position = self._random_position()

    def _random_position(self):
        max_x = (WIDTH - CELL_SIZE) // CELL_SIZE
        max_y = (HEIGHT - CELL_SIZE) // CELL_SIZE
        x = random.randint(0, max_x) * CELL_SIZE
        y = random.randint(0, max_y) * CELL_SIZE
        return x, y

    def draw(self, surface):
        rect = pygame.Rect(
            self.position[0], self.position[1], CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(surface, RED, rect)