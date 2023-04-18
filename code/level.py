import pygame
from settings import * 
from player import Player
from debug import debug
from support import *
from random import choice
from inventory_menu import *
from level1 import Level1
from level2 import Level2
from level_home import Level_home
from quest import Journal

class Level:
    def __init__(self):
        self.current_quest=1
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
        self.level_2 = Level2(self.player)
        self.level_home = Level_home(self.player)
        self.create_map(self.level_1)
        # self.player = Player((550/16*TILESIZE, 450/16*TILESIZE), [self.visible_sprites], self.obstacle_sprites, 
        #                      self.pickup_sprites, self.visible_sprites, self.entrance_sprites)
        #self.potion = Potionmaker((550/16*TILESIZE, 450/16*TILESIZE), [self.visible_sprites])
        #----
        #journal
        self.journal = Journal(self.scroll_index, self.current_quest)

    def create_map(self, current_level):
        #current_level=Level1()
        self.current_level = current_level
        self.visible_sprites = current_level.get_visible_sprites()
        self.entrance_sprites = current_level.get_door_sprites()
        self.obstacle_sprites = current_level.get_obstacle_sprites()
        self.pickup_sprites = current_level.get_pickup_sprites()
        self.portal_sprites = current_level.get_portal_sprites()
        self.visible_sprites.add(self.visible_sprites_player)
        self.player.update_sprites(self.visible_sprites, self.entrance_sprites, 
                                   self.obstacle_sprites, self.pickup_sprites, self.portal_sprites)
    def show_this(self, open_this):
        self.scroll_index[0] = 0 
        self.game_paused = not self.game_paused
        self.open_this = open_this #inventory or journal
        
    def check_collision(self, check_sprites):
        if check_sprites is not None:
            for sprite in check_sprites:
                if sprite.hitbox.colliderect(self.player.hitbox):
                    return True
        return False
        #debug("blob",10,100)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        if self.check_collision(self.entrance_sprites) is True:
            if(self.current_level==self.level_1):
                self.create_map(self.level_home)
                self.player.teleport((750,950))
                self.visible_sprites.add(self.player)
            elif(self.current_level==self.level_home):
                self.create_map(self.level_1)
                self.player.teleport((950, 900))
                self.visible_sprites.add(self.player)
            elif(self.current_level==self.level_2):
                debug("It's too dark there")
        if self.check_collision(self.portal_sprites) is True:
            if self.current_level == self.level_home:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    self.create_map(self.level_2)
                    self.player.teleport((400, 900))
                if keys[pygame.K_SPACE]:
                    if self.journal.get_quest_item() in self.player.get_inventory():
                        self.player.inventory[self.journal.get_quest_item()]-=1
                        if self.player.inventory[self.journal.get_quest_item()] == 0:
                            self.player.inventory.pop(self.journal.get_quest_item())
                        
                        if 'Gold' in self.player.inventory:
                            self.player.inventory['Gold']+=self.current_quest*10
                        else:
                            self.player.inventory['Gold'] = self.current_quest*10

                        self.current_quest+=1
                        self.journal.change_quest(self.current_quest)
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    self.create_map(self.level_home)
                    self.player.teleport((640, 800))
        if self.game_paused and self.open_this=='inventory':
            self.inventory_menu.update_inventory(self.player.get_inventory(),self.scroll_index)
            self.inventory_menu.display()
            self.visible_sprites.update()
        elif self.game_paused and self.open_this =='journal':
            self.journal.update_journal(self.scroll_index)
            self.journal.display()
            keys = pygame.key.get_pressed()
            # if keys[pygame.K_e]:
            #     self.journal.change_quest(2)
        else:
            self.visible_sprites.update()