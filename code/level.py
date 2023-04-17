import pygame
from settings import * 
from player import Player
from debug import debug
from support import *
from random import choice
from inventory_menu import *
from level1 import Level1
from level_home import Level_home
from potionmaker import Potionmaker

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites_player = pygame.sprite.Group()
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
        self.player = Player((550/16*TILESIZE, 450/16*TILESIZE), [self.visible_sprites_player])
        self.level_1 = Level1(self.player)
        self.level_home = Level_home(self.player)
        self.create_map(self.level_1)
        #----
        #portal

    def create_map(self, current_level):
        #current_level=Level1()
        self.current_level = current_level
        self.visible_sprites = current_level.get_visible_sprites()
        self.entrance_sprites = current_level.get_door_sprites()
        self.obstacle_sprites = current_level.get_obstacle_sprites()
        self.pickup_sprites = current_level.get_pickup_sprites()
        self.visible_sprites.add(self.visible_sprites_player)
        self.player.update_sprites(self.visible_sprites, self.entrance_sprites, self.obstacle_sprites, self.pickup_sprites)
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
            if(self.current_level==self.level_1):
                self.create_map(self.level_home)
                self.player.teleport((750,950))
                self.visible_sprites.add(self.player)
            elif(self.current_level==self.level_home):
                self.create_map(self.level_1)
                self.player.teleport((950, 900))
                self.visible_sprites.add(self.player)
        if self.game_paused:
            self.inventory_menu.update_inventory(self.player.get_inventory(), self.scroll_index)
            self.inventory_menu.display()
            self.visible_sprites.update()
        else:
            self.visible_sprites.update()