import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, (0, 255, 0), (self.left + self.cell_size * j,
                                                               self.top + self.cell_size * i, self.cell_size,
                                                               self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (self.left + self.cell_size * j,
                                                           self.top + self.cell_size * i, self.cell_size,
                                                           self.cell_size), 1)

    def get_cell(self, mouse_pos):
        mx, my = mouse_pos
        for i in range(self.height):
            for j in range(self.width):
                a = self.left + self.cell_size * j
                b = self.top + self.cell_size * i
                if mx in range(a, a + self.cell_size) and my in range(b, b + self.cell_size):
                    return (j, i)

    def on_click(self, cell_coords):
        if cell_coords:
            x, y = cell_coords
            for i in range(self.height):
                for j in range(self.width):
                    if i == y and j == x:
                        if self.board[i][j] == 0:
                            self.board[i][j] = 1
                        elif self.board[i][j] == 1:
                            self.board[i][j] = 0

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        # print(cell)
        self.on_click(cell)