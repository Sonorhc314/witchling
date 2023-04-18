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
            # 'fire potion' : ['big sunflower', 'daybloom']
            'fire potion' : ['clover', 'nettle']
        }
        self.ENTER = "                                                        "   # ends col:79
        self.BOTTOM_TEXT = "    Craft [K]                       Next [SPACE]        "  # ends col:85
        self.BOTTOM_TEXT_NO_CRAFT = "                                    Next [SPACE]        "  # ends col:94
                                                                                        # Craft [K] Next [SPACE]

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
            self.craftable_list = []
        elif keys[pygame.K_k] and self.player_choice == None:
            self.player_choice = self.menu.get_scroll_index()[0]
            self.craft_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        if self.player_choice is not None:
            if current_time-self.craft_time > 1000:
                self.player_choice = None
        # debug(self.player_choice)

        

    
        
    def craft(self):
        # if len(self.craftable_list) == 0:
        player_inventory = self.player.get_inventory()
        craftable_list = []
        # find what you can craft
        for potion, ingredients in self.potion_list.items():
            potion_ready = True
            for ingredient in ingredients:
                if ingredient not in player_inventory or player_inventory[ingredient]<ingredients.count(ingredient):
                    potion_ready = False
            if potion_ready:
                craftable_list.append(potion)

        # show what you can craft
        self.do_dialog(craftable_list)

        # now craft, duh
        if self.player_choice!=None and self.player_choice!='Blocked' and abs(self.player_choice-1) < len(craftable_list):
            debug(f"Crafting {craftable_list[self.player_choice-1]}")
            potion_to_craft = craftable_list[self.player_choice-1]
            for ingredient in self.potion_list[potion_to_craft]:
                self.player.inventory[ingredient]-=1
                if self.player.inventory[ingredient] == 0:
                    self.player.inventory.pop(ingredient)
            if potion in self.player.inventory.keys():
                self.player.inventory[potion]+=1
            else:
                self.player.inventory[potion] = 1
            self.player_choice = 'Blocked'



    

    def do_dialog(self, craftable_list):
        if len(craftable_list)>0:
            to_print = f"Hm' what should I do?/"
            while len(to_print)<=55:
                to_print+=' '
            to_print+= self.ENTER+self.BOTTOM_TEXT_NO_CRAFT
            for potion in craftable_list:
                to_print+=potion
                for i in range(56-len(potion)):
                    to_print+=' '
                to_print+= self.ENTER+self.BOTTOM_TEXT
            self.menu.set_text(to_print)
            self.display_menu_flag = True
        else:
            to_print = f"Uh' I  should  look  for  more  ingredients  rly  soon!"
            self.menu.set_text(to_print)
            self.display_menu_flag = True

        


