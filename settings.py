import pygame

# основные настройки игры
FPS = 60
screen_size = width, height = (1200, 800)

tile_width = tile_height = 50

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
player_group = pygame.sprite.Group()
