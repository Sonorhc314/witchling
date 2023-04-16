import pygame
from settings import * 
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from inventory_menu import *
from potionmaker import Potionmaker

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()
        self.portal_sprites = pygame.sprite.Group()
        self.game_paused = False
        #----
        #inventory
        self.scroll_index = [0]
        self.reading_time = None
        self.inventory_menu = Inventory_menu(self.scroll_index)
        self.reading = False
        self.scroll_cooldown = 300
        self.flowers = {0: 'sunflower', 1: 'big sunflower', 2: 'clover', 
                        3:'bootyflower', 4:'nettle', 5:'soft nettle', 6:'daybloom'}
        self.create_map()
        #----
        #portal

    def create_map(self):
        layout = {
            # 'grass': import_csv_layout('map\map_Grass.csv'),
            'house': import_csv_layout('graphics\map\map_house.csv'),
            'portal': import_csv_layout('graphics\map\map_portal.csv'),
            'item': import_csv_layout('graphics\map\map_items.csv'),
            'tree': import_csv_layout('graphics\map\map_forest.csv'),
            'object': import_csv_layout('graphics\map\map_objects.csv')
        }
        graphics = {
            # 'grass': import_folder('graphics\Grass'),
            'house': import_folder('graphics\house'),
            'object': import_folder('graphics\object'),
            'tree': import_folder('graphics\objects\\trees'),
            'item': import_folder('graphics\\items\\flowers')
        }
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col!='-1':
                        x=col_index*TILESIZE
                        y=row_index*TILESIZE
                        if style == 'house':
                            surf = graphics['house'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'invisible', surf)
                        
                        if style =='object':
                            #pass 
                            Tile((x,y), [self.obstacle_sprites], 'object')

                        if style == 'portal':
                            Tile((x,y), [self.portal_sprites], 'portal')

                        if style =='tree':
                            surf = graphics['tree'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'tree', surf)

                        if style =='item':
                            #print(graphics['entity'])
                            #graphics['entity'][0]
                            surf = graphics['item'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.pickup_sprites], 'item', surf, self.flowers.get(int(col)))
        #         if col == 'x':
        #             Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        #         elif col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player((550/16*TILESIZE, 450/16*TILESIZE), [self.visible_sprites], self.obstacle_sprites, 
                             self.pickup_sprites, self.visible_sprites, self.portal_sprites)
        Potionmaker((600/16*TILESIZE, 450/16*TILESIZE), [self.visible_sprites], self.player)
    def inventory_show(self):
        self.game_paused = not self.game_paused
        
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        if self.game_paused:
            self.inventory_menu.update_inventory(self.player.get_inventory(), self.scroll_index)
            self.inventory_menu.display()
            self.visible_sprites.update()
        else:
            self.visible_sprites.update()
        #debug(self.player.status)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] //2
        self.half_height = self.display_surface.get_size()[1] //2
        self.offset = pygame.math.Vector2()

        self.floor_surface = my_load('graphics/map/map.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))
    
    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_offset_pos = self.floor_rect.topleft - self.offset

        self.display_surface.blit(self.floor_surface, floor_offset_pos)
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)