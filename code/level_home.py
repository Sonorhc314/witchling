import pygame
from settings import * 
from tile import Tile
from debug import debug
from support import *
from camera import YSortCameraGroup
from potionmaker import Potionmaker

class Level_home:
    def __init__(self, player):
        self.player = player
        self.visible_sprites = YSortCameraGroup('graphics/map_house/map_house.png')
        self.obstacle_sprites = pygame.sprite.Group()
        self.door_sprites = pygame.sprite.Group()
        self.pickup_sprites = pygame.sprite.Group()
        self.portal_sprites = pygame.sprite.Group()
        self.flowers = {0: 'sunflowere', 1: 'big sunflower', 2: 'clover', 
                        3:'bootyflower', 4:'nettle', 5:'soft nettle', 6:'daybloom'}
        self.create_tiles()
        Potionmaker((self.x_alchemy, self.y_alchemy), [self.visible_sprites], self.player)
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
            'border': import_csv_layout('graphics\map_house\\map_house_border.csv'),
            'portal': import_csv_layout('graphics\map_house\map_house_portal.csv'),
            'alchemy': import_csv_layout('graphics\map_house\map_house_alchemy.csv'),
            'object': import_csv_layout('graphics\map_house\map_house_objects.csv'),
            'entrance': import_csv_layout('graphics\map_house\map_house_house.csv')
        }
        self.graphics = {
            #'border': import_folder('graphics\Grass'),
            'portal': import_folder('graphics\portal'),
            'object': import_folder('graphics\object'),
            'alchemy': import_folder('graphics\\alchemy')
        }
        for style, layout in self.layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col!='-1':
                        x=col_index*TILESIZE
                        y=row_index*TILESIZE
                        # if style == 'house': #21,22,25,26
                        #     surf = self.graphics['house'][int(col)]
                        #     if int(col) in [25,26]:
                        #         #print(int(col))
                        #         Tile((x,y), [self.visible_sprites, self.door_sprites], 'invisible', surf, inflate=True)
                        #     else:
                        #         print(int(col))
                        #         surf = self.graphics['house'][int(col)]
                        #         Tile((x,y), [self.visible_sprites], 'invisible', surf)
                        if style == 'entrance':
                            if int(col) in [505,506,507]:
                                Tile((x,y), [self.door_sprites], 'invisible')
                        
                        if style == 'alchemy':
                            if int(col)==326:
                                self.x_alchemy=x
                                self.y_alchemy=y
                                print(col)
                                #print(indexes.get(int(col)))
                                surf = self.graphics['alchemy'][0]
                                Tile((x,y), [self.visible_sprites], 'alchemy', surf)
                        
                        if style =='object':
                            #pass 
                            #print(col)
                            Tile((x,y), [self.obstacle_sprites], 'invisible')

                        if style =='border':
                            #surf = self.graphics['border'][int(col)]
                            Tile((x,y), [self.obstacle_sprites], 'invisible')

                        if style =='portal':
                            indexes = {1:0,2:1,33:2,34:3,65:4, 66:5, 97:6,98:7}
                            surf = self.graphics['portal'][indexes[int(col)]]
                            Tile((x,y), [self.visible_sprites, self.portal_sprites], 'portal', surf)

                        # if style =='portal':
                        #     #print(graphics['entity'])
                        #     #graphics['entity'][0]
                        #     #surf = self.graphics['item'][int(col)]
                        #     Tile((x,y), [self.visible_sprites, self.pickup_sprites], 'item', surf, name=self.flowers.get(int(col)))
    