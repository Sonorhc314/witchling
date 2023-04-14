import pygame
from settings import * 
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE)), name=None):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.name = name
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1]))
        else:
            self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.surface = surface
    def get_surface(self):
        return self.surface
    def get_name(self):
        return self.name