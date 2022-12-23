import pygame

from load_image import load_image
from settings import tile_width, tile_height, all_sprites, player_group, tiles, width, height

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}

player_image = load_image('mar.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, x, y):
        super(Tile, self).__init__(tiles, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * x, tile_height * y
        )


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.x = pos_x
        self.y = pos_y
        self.pressed_w = True
        self.pressed_a = True
        self.pressed_s = True
        self.pressed_d = True

    def update(self, level_map):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pressed_w and level_map[self.y - 1][self.x] != '#':
            self.y += -1
            self.pressed_w = False
        elif not keys[pygame.K_w]:
            self.pressed_w = True

        if keys[pygame.K_a] and self.pressed_a and level_map[self.y][self.x - 1] != '#':
            self.x += -1
            self.pressed_a = False
        elif not keys[pygame.K_a]:
            self.pressed_a = True

        if keys[pygame.K_s] and self.pressed_s and level_map[self.y + 1][self.x] != '#':
            self.y += 1
            self.pressed_s = False
        elif not keys[pygame.K_s]:
            self.pressed_s = True

        if keys[pygame.K_d] and self.pressed_d and level_map[self.y][self.x + 1] != '#':
            self.x += 1
            self.pressed_d = False
        elif not keys[pygame.K_d]:
            self.pressed_d = True

        self.rect.x = self.x * tile_width + 15
        self.rect.y = self.y * tile_height + 5


# class Camera:
#     # зададим начальный сдвиг камеры
#     def __init__(self):
#         self.dx = 0
#         self.dy = 0
#
#     # сдвинуть объект obj на смещение камеры
#     def apply(self, obj):
#         obj.rect.x += self.dx
#         obj.rect.y += self.dy
#
#     # позиционировать камеру на объекте target
#     def update(self, target):
#         self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
#         self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)
#         print(self.dx, self.dy)
