import sys
import pygame

from settings import FPS, all_sprites, tiles, player_group
from load_map import load_level
from tiles import Tile, Player


def generate_level(level_map):
    new_player, x, y = None, None, None
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == '.':
                Tile('empty', x, y)
            elif level_map[y][x] == '#':
                Tile('wall', x, y)
            elif level_map[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def game_sicle(screen, clock):
    level_map = load_level('lvl_1.txt')
    player, map_width, map_height = generate_level(level_map)
    # camera = Camera()
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # camera.update(player)
        # for sprite in all_sprites:
        #     camera.apply(sprite)
        player_group.update(level_map)
        all_sprites.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
