import os
import sys
import pygame


def load_image(name, color_key=None):
    full_path = os.path.join('images', name)
    if not os.path.isfile(full_path):
        print(f'image {name} is not found')
        sys.exit()
    image = pygame.image.load(full_path)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image.convert_alpha()
    return image
