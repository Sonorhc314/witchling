import pygame
from settings import * 
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE)), inflate=False, name=None):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        self.name = name
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
        if sprite_type == 'item':
            self.hitbox = self.rect.inflate(-15,-15)
        self.surface = surface
    def get_surface(self):
        return self.surface
    def get_name(self):
        return self.name