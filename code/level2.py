import pygame
from settings import * 
from tile import Tile
from debug import debug
from support import *
from camera import YSortCameraGroup

class Level2:
    def __init__(self, player):
        self.player = player # currently not used
        self.visible_sprites = YSortCameraGroup('graphics/map_island/island.png')
        self.obstacle_sprites = pygame.sprite.Group()
        self.door_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()
        self.portal_sprites = pygame.sprite.Group()
        self.flowers = {0: 'sunflowere', 1: 'big sunflower', 2: 'clover', 
                        3:'bootyflower', 4:'nettle', 5:'soft nettle', 6:'daybloom'}
        self.create_tiles()
    def get_visible_sprites(self):
        return self.visible_sprites
    def get_obstacle_sprites(self):
        return self.obstacle_sprites
    def get_door_sprites(self):
        return self.door_sprites
    def get_pickup_sprites(self):
        return self.pickup_sprites
    def get_portal_sprites(self):
        return self.portal_sprites
    def create_tiles(self):
        self.layout = {
            # 'grass': import_csv_layout('map\map_Grass.csv'),
            'cave': import_csv_layout('graphics\map_island\island_cave.csv'),
            'portal': import_csv_layout('graphics\map_island\island_portal.csv'),
            'item': import_csv_layout('graphics\map_island\island_items.csv'),
            'river': import_csv_layout('graphics\map_island\island_river.csv'),
            'object': import_csv_layout('graphics\map_island\island_objects.csv')
        }
        self.graphics = {
            # 'grass': import_folder('graphics\Grass'),
            'cave': import_folder('graphics\cave'),
            # 'object': import_folder('graphics\object'),
            # 'tree': import_folder('graphics\objects\\trees'),
            'portal': import_folder('graphics\portal'),
            'item': import_folder('graphics\\items\\flowers')
        }
        for style, layout in self.layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col!='-1':
                        x=col_index*TILESIZE
                        y=row_index*TILESIZE
                        if style == 'cave': #21,22,25,26
                            #surf = self.graphics[''][int(col)]
                            if int(col) in [111, 112, 113]:
                                #print(int(col))
                                Tile((x,y), [self.door_sprites], 'invisible', inflate=True)
                            else:
                                #surf = self.graphics['cave'][int(col)]
                                Tile((x,y), [self.obstacle_sprites], 'invisible')
                        
                        if style =='object':
                            #pass 
                            Tile((x,y), [self.obstacle_sprites], 'object')

                        if style =='river':
                            Tile((x,y), [self.obstacle_sprites], 'river')

                        if style =='item':
                            surf = self.graphics['item'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.pickup_sprites], 'item', surf, name=self.flowers.get(int(col)))
                        if style =='portal':
                            #pass 
                            indexes = {1:0,2:1,33:2,34:3,65:4,66:5,97:6,98:7}
                            surf = self.graphics['portal'][indexes[int(col)]]
                            Tile((x,y), [self.visible_sprites, self.portal_sprites], 'portal', surf)
    