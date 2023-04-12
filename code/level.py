import pygame
from settings import * 
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from inventory_menu import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()
        self.game_paused = False
        self.create_map()
        #inventory
        self.inventory_menu = Inventory_menu(self.player.get_inventory())
    def create_map(self):
        layout = {
            'boundary': import_csv_layout('graphics\map\map_border.csv'),
            # 'grass': import_csv_layout('map\map_Grass.csv'),
            'object': import_csv_layout('graphics\map\map_house.csv'),
            # 'entity': import_csv_layout('map\map_Entities.csv')
        }
        graphics = {
            # 'grass': import_folder('graphics\Grass'),
            # 'object': import_folder('graphics\objects'),
            # 'entity': import_folder('graphics\monsters\\bamboo\idle')
        }
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col!='-1':
                        x=col_index*TILESIZE
                        y=row_index*TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        
                        if style =='grass':
                            #pass 
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'grass', choice(graphics['grass']))
                        
                        if style =='object':
                            #surf = graphics['object'][int(col)]
                            Tile((x,y), [self.obstacle_sprites], 'object')

                        if style =='entity':
                            Tile((x,y), [self.visible_sprites, self.pickup_sprites], 'entity', choice(graphics['entity']))
        #         if col == 'x':
        #             Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        #         elif col == 'p':
        #             self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player((200/16*TILESIZE, 200/16*TILESIZE), [self.visible_sprites], self.obstacle_sprites, 
                             self.pickup_sprites, self.visible_sprites)
    def inventory_show(self):
        self.game_paused = not self.game_paused
        
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        if self.game_paused:
            self.inventory_menu.display()
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