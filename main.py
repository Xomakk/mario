import sys
from random import randint

import pygame

from Board import Board
from copy import deepcopy


class Minesweeper(Board):
    def __init__(self, width, height, count_bombs):
        super(Minesweeper, self).__init__(width, height)
        self.count_bombs = count_bombs

        self.board = [[-1] * width for _ in range(height)]

        for _ in range(count_bombs):
            x, y = randint(0, width - 1), randint(0, height - 1)
            self.board[y][x] = 10

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] != -1:
                    num = pygame.font.Font(None, 42).render(f'{self.board[i][j]}', True, (0, 255, 0))
                    screen.blit(num, (self.left + self.cell_size * j + 5, self.top + self.cell_size * i + 5))

                if self.board[i][j] == 10:
                    pygame.draw.rect(screen, (255, 0, 0), (self.left + self.cell_size * j,
                                                           self.top + self.cell_size * i, self.cell_size,
                                                           self.cell_size))

                pygame.draw.rect(screen, (255, 255, 255), (self.left + self.cell_size * j,
                                                           self.top + self.cell_size * i, self.cell_size,
                                                           self.cell_size), 1)

    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            for i in range(self.height):
                for j in range(self.width):
                    if i == y and j == x:
                        self.open_cell(i, j)

    def open_cell(self, i, j):
        if self.board[i][j] != 10:
            self.board[i][j] = self.search_bombs(i, j)

    def search_bombs(self, i, j):
        copy_board = deepcopy(self.board)
        count_neighbor = 0

        if i != 0:
            if copy_board[i - 1][j] == 10:
                count_neighbor += 1
        if i != self.height - 1:
            if copy_board[i + 1][j] == 10:
                count_neighbor += 1
        if j != 0:
            if copy_board[i][j - 1] == 10:
                count_neighbor += 1
        if j != self.width - 1:
            if copy_board[i][j + 1] == 10:
                count_neighbor += 1

        if i != 0 and j != 0:
            if copy_board[i - 1][j - 1] == 10:
                count_neighbor += 1
        if i != self.height - 1 and j != self.width - 1:
            if copy_board[i + 1][j + 1] == 10:
                count_neighbor += 1
        if j != 0 and i != self.height - 1:
            if copy_board[i + 1][j - 1] == 10:
                count_neighbor += 1
        if j != self.width - 1 and i != 0:
            if copy_board[i - 1][j + 1] == 10:
                count_neighbor += 1

        return count_neighbor


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 1000

    cell_size = 40
    count_cell_x = (width - 20) // cell_size
    count_cell_y = (height - 20) // cell_size

    count_bombs = 10
    board = Minesweeper(count_cell_x, count_cell_y, count_bombs)
    board.set_view(10, 10, cell_size)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 10

    running = True
    while running:
        screen.fill((0, 0, 0))
        board.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    pass
                if event.button == 1:
                    board.get_click(event.pos)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
