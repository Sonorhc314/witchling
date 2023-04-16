import pygame
from settings import * 
from debug import debug
import dialog

class Potionmaker(pygame.sprite.Sprite):
    def __init__(self, pos, groups, player, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)

        self.menu = dialog.Dialog(0, WITCH_NAME, "Hm, what should I do?")
        self.player = player
        self.couldron = []
        self.potion_list = {
            'wind potion' : ['clover', 'soft nettle'],
            'fire potion' : ['big sunflower', 'daybloom']
        }

        self.display_menu_flag = False
        self.interracted_flag = False

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
        self.menu.set_text(f"Let's see what I have...: {craftable_list}")
        self.display_menu_flag = True

        


