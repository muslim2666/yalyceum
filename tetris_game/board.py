import pygame

from tetris_game.tetromino import Tetromino
from settings import (
    WIDTH,
    HEIGHT,
    CELL_SIZE,
    BLACK,
    CYAN,
    WHITE,
)


COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE


class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        start_x = COLS // 2 - 1
        self.current = Tetromino(start_x, 0)

    def valid_position(self, shape, offset):
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if not cell:
                    continue

                new_x = x + off_x
                new_y = y + off_y

                if (
                    new_x < 0
                    or new_x >= COLS
                    or new_y >= ROWS
                    or self.grid[new_y][new_x]
                ):
                    return False

        return True

    def freeze(self):
        for y, row in enumerate(self.current.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current.y + y][
                                 self.current.x + x
                                 ] = 1

        self.clear_lines()
        start_x = COLS // 2 - 1
        self.current = Tetromino(start_x, 0)

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(v == 0 for v in row)]
        lines_cleared = ROWS - len(new_grid)
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(COLS)])

        self.grid = new_grid

    def draw(self, surface):
        surface.fill(BLACK)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        x * CELL_SIZE,
                        y * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                    )
                    pygame.draw.rect(surface, CYAN, rect)

        for y, row in enumerate(self.current.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (self.current.x + x) * CELL_SIZE,
                        (self.current.y + y) * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                    )
                    pygame.draw.rect(surface, WHITE, rect)