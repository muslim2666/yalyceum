import pygame

from settings import CELL_SIZE, GREEN


class Snake:
    def __init__(self, position):
        head = position
        self.body = [
            head,
            (head[0] - CELL_SIZE, head[1]),
            (head[0] - 2 * CELL_SIZE, head[1]),
        ]
        self.direction = pygame.K_RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        moves = {
            pygame.K_UP: (0, -CELL_SIZE),
            pygame.K_DOWN: (0, CELL_SIZE),
            pygame.K_LEFT: (-CELL_SIZE, 0),
            pygame.K_RIGHT: (CELL_SIZE, 0),
        }
        dx, dy = moves.get(self.direction, (0, 0))
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, key):
        opposites = {
            pygame.K_UP: pygame.K_DOWN,
            pygame.K_DOWN: pygame.K_UP,
            pygame.K_LEFT: pygame.K_RIGHT,
            pygame.K_RIGHT: pygame.K_LEFT,
        }
        if key != opposites.get(self.direction):
            self.direction = key

    def draw(self, surface):
        for segment in self.body:
            rect = pygame.Rect(
                segment[0], segment[1], CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(surface, GREEN, rect)