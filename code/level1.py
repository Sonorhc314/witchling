import pygame
from settings import * 
from tile import Tile
from debug import debug
from support import *
from camera import YSortCameraGroup

class Level1:
    def __init__(self):
        self.visible_sprites = YSortCameraGroup('graphics/map/map.png')
        self.obstacle_sprites = pygame.sprite.Group()
        self.door_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()
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
    def create_tiles(self):
        self.layout = {
            # 'grass': import_csv_layout('map\map_Grass.csv'),
            'house': import_csv_layout('graphics\map\map_house.csv'),
            'portal': import_csv_layout('graphics\map\map_portal.csv'),
            'item': import_csv_layout('graphics\map\map_items.csv'),
            'tree': import_csv_layout('graphics\map\map_forest.csv'),
            'object': import_csv_layout('graphics\map\map_objects.csv')
        }
        self.graphics = {
            # 'grass': import_folder('graphics\Grass'),
            'house': import_folder('graphics\house'),
            'object': import_folder('graphics\object'),
            'tree': import_folder('graphics\objects\\trees'),
            'item': import_folder('graphics\\items\\flowers')
        }
        for style, layout in self.layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col!='-1':
                        x=col_index*TILESIZE
                        y=row_index*TILESIZE
                        if style == 'house': #21,22,25,26
                            surf = self.graphics['house'][int(col)]
                            if int(col) in [25,26]:
                                #print(int(col))
                                Tile((x,y), [self.visible_sprites, self.door_sprites], 'invisible', surf, inflate=True)
                            else:
                                print(int(col))
                                surf = self.graphics['house'][int(col)]
                                Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'invisible', surf)
                        
                        if style =='object':
                            #pass 
                            Tile((x,y), [self.obstacle_sprites], 'object')

                        if style =='tree':
                            surf = self.graphics['tree'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'tree', surf)

                        if style =='item':
                            #print(graphics['entity'])
                            #graphics['entity'][0]
                            surf = self.graphics['item'][int(col)]
                            Tile((x,y), [self.visible_sprites, self.pickup_sprites], 'item', surf, name=self.flowers.get(int(col)))
    