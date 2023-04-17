import pygame
from settings import * 
from debug import debug
import dialog
from support import *

class Potionmaker(pygame.sprite.Sprite):
    def __init__(self, pos, groups, player, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.image = my_load('graphics\\alchemy\\326.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)

        self.menu = dialog.Dialog(0, WITCH_NAME, "Hm, what should I do?")
        self.player = player
        self.couldron = []
        self.potion_list = {
            'wind potion' : ['clover', 'soft nettle'],
            'fire potion' : ['big sunflower', 'daybloom']
        }
        self.ENTER = "                                                  "

        self.display_menu_flag = False
        self.interracted_flag = False
        self.player_choice =None
        self.craft_time = 0

    def update(self): ##-----------------------
        self.input()
        if self.interracted_flag:
            self.craft()
            self.menu.display()
        # self.display_menu()

    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and self.player.hitbox.colliderect(self.hitbox):
            self.interracted_flag = True
        elif keys[pygame.K_ESCAPE] or not self.player.hitbox.colliderect(self.hitbox):
            self.interracted_flag = False
        elif keys[pygame.K_k]:
            self.player_choice = self.menu.get_scroll_index()
            self.craft_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        if self.player_choice is not None:
            if current_time-self.craft_time > 100:
                self.player_choice = None
        debug(self.player_choice)

        

    
        
    def craft(self):
        player_inventory = self.player.get_inventory()
        craftable_list = []
        # find what you can craft
        for potion, ingredients in self.potion_list.items():
            potion_ready = True
            for ingredient in ingredients:
                if ingredient not in player_inventory:
                    potion_ready = False
            if potion_ready:
                craftable_list.append(potion)

        # show what you can craft
        # menu = dialog.Dialog("Hm, lets see what we can do here..", WITCH_NAME)
        to_print = "Hm, what should I do?/"
        to_print+= self.ENTER + self.ENTER + f"{craftable_list}"
        self.menu.set_text(to_print)
        self.display_menu_flag = True
        
        


