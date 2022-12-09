import sys
import pygame

from Board import Board
from copy import deepcopy


# Каждое следующее поколение рассчитывается на основе предыдущего по таким правилам:
#   в пустой (мёртвой) клетке, с которой соседствуют три живые клетки, зарождается жизнь;
#   если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае
#   (если живых соседей меньше двух или больше трёх) клетка умирает («от одиночества» или «от перенаселённости»).

# Игра прекращается, если
#    на поле не останется ни одной «живой» клетки;
#   конфигурация на очередном шаге в точности (без сдвигов и поворотов) повторит себя же на одном из более ранних шагов
#   (складывается периодическая конфигурация)
#   при очередном шаге ни одна из клеток не меняет своего состояния (предыдущее правило действует на один шаг назад,
#   складывается стабильная конфигурация)

class Life(Board):
    def __init__(self, width, height):
        super(Life, self).__init__(width, height)

    def next_move(self):
        copy_board = deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                life_value = copy_board[i][j]
                count_neighbor = 0

                if i != 0:
                    if copy_board[i - 1][j] == 1:
                        count_neighbor += 1
                if i != self.height - 1:
                    if copy_board[i + 1][j] == 1:
                        count_neighbor += 1
                if j != 0:
                    if copy_board[i][j - 1] == 1:
                        count_neighbor += 1
                if j != self.width - 1:
                    if copy_board[i][j + 1] == 1:
                        count_neighbor += 1

                if i != 0 and j != 0:
                    if copy_board[i - 1][j - 1] == 1:
                        count_neighbor += 1
                if i != self.height - 1 and j != self.width - 1:
                    if copy_board[i + 1][j + 1] == 1:
                        count_neighbor += 1
                if j != 0 and i != self.height - 1:
                    if copy_board[i + 1][j - 1] == 1:
                        count_neighbor += 1
                if j != self.width - 1 and i != 0:
                    if copy_board[i - 1][j + 1] == 1:
                        count_neighbor += 1

                if life_value == 0:
                    if count_neighbor == 3:
                        self.board[i][j] = 1

                if life_value == 1:
                    if not (count_neighbor in [2, 3]):
                        self.board[i][j] = 0


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 1000

    cell_size = 40
    count_cell_y = (width - 20) // cell_size
    count_cell_x = (height - 20) // cell_size

    board = Life(count_cell_x, count_cell_y)
    board.set_view(10, 10, cell_size)

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 10

    simulated = False
    running = True
    while running:
        screen.fill((0, 0, 0))
        board.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulated = not simulated
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    simulated = not simulated
                if event.button == 1:
                    board.get_click(event.pos)
        if simulated:
            board.next_move()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
