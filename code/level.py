import pygame
from settings import * 
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from inventory_menu import *
from camera import YSortCameraGroup
from level1 import Level1
from level_home import Level_home

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.door_sprites = pygame.sprite.Group()
        self.game_paused = False
        #----
        #inventory
        self.scroll_index = [0]
        self.reading_time = None
        self.inventory_menu = Inventory_menu(self.scroll_index)
        self.reading = False
        self.scroll_cooldown = 300
        self.flowers = {0: 'sunflowere', 1: 'big sunflower', 2: 'clover', 
                        3:'bootyflower', 4:'nettle', 5:'soft nettle', 6:'daybloom'}
        self.level_1 = Level1()
        self.level_home = Level_home()
        self.create_map(self.level_1)
        self.player = Player((550/16*TILESIZE, 450/16*TILESIZE), [self.visible_sprites], self.obstacle_sprites, 
                             self.pickup_sprites, self.visible_sprites, self.entrance_sprites)
        #----
        #portal

    def create_map(self, current_level):
        # current_level=Level1()
        self.visible_sprites = current_level.get_visible_sprites()
        self.entrance_sprites = current_level.get_door_sprites()
        self.obstacle_sprites = current_level.get_obstacle_sprites()
        self.pickup_sprites = current_level.get_pickup_sprites()
    def inventory_show(self):
        self.game_paused = not self.game_paused
        
    def entrance_collision(self):
        if self.entrance_sprites is not None:
            for sprite in self.entrance_sprites:
                if sprite.hitbox.colliderect(self.player.hitbox):
                    return True
        return False
        #debug("blob",10,100)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        if self.entrance_collision() is True:
            self.create_map(self.level_home)
            self.visible_sprites.add(self.player)
        if self.game_paused:
            self.inventory_menu.update_inventory(self.player.get_inventory(), self.scroll_index)
            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()
            if self.reading:
                if current_time - self.reading_time >= self.scroll_cooldown:
                    self.reading=False
            if keys[pygame.K_SPACE] and not self.reading:
                self.reading = True
                self.reading_time = pygame.time.get_ticks()
                print(self.scroll_index[0])
                self.scroll_index[0]+=1
            self.inventory_menu.display()
        else:
            self.visible_sprites.update()
        #debug(self.player.status)