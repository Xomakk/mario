import sys
import pygame
from settings import screen_size

pygame.init()
screen = pygame.display.set_mode(screen_size)

from game import game_sicle
from menu import main_menu

if __name__ == '__main__':
    clock = pygame.time.Clock()

    # заставка для игры
    main_menu(screen, clock)
    # сама игра
    game_sicle(screen, clock)

pygame.quit()
