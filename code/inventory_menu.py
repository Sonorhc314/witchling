import pygame
from settings import *

class Inventory_menu:
    def __init__(self, inventory):
        self.display_surface = pygame.display.get_surface()
        self.inventory = inventory
        #self.rect = pygame.Rect(WIDTH/4,HEIGHT/4,WIDTH/2, HEIGHT/2)
        self.menu_width = 160
        self.menu_height = 160
        self.rect_items = pygame.Rect(WIDTH/4,HEIGHT/4,self.menu_width, self.menu_height)
        self.rect_player = pygame.Rect(WIDTH/2,HEIGHT/4,self.menu_width, self.menu_height)
        self.image = pygame.image.load("graphics\player\down\down_0.png")
        self.grid_size_x = 80
        self.grid_size_y = 92
        # self.picture_width = 160
        # self.picture_height = 270
    def display(self):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        #pygame.draw.rect(self.display_surface, "blue", self.rect)
        pygame.draw.rect(self.display_surface, "white", self.rect_items)
        
        # for x in range(self.rect_items.x, self.rect_items.x + self.menu_width, self.grid_size_x):
        #     pygame.draw.line(self.display_surface, (0, 0, 0), (x, self.rect_items.y), (x, self.rect_items.y + HEIGHT/2), 3)

        # for y in range(self.rect_items.y, self.rect_items.y + self.menu_height, self.grid_size_y):
        #     pygame.draw.line(self.display_surface, (0, 0, 0), (self.rect_items.x, y), (self.rect_items.x+WIDTH/2, y), 3)

        # # Calculate the number of rows and columns in the grid
        # num_rows = self.rect_items.height // self.grid_size_x
        # num_cols = self.rect_items.width // self.grid_size_x

        # flag_end = False
        # fill=0
        # for row in range(num_rows):
        #     if flag_end:
        #         break
        #     for col in range(num_cols):
        #         if fill<len(self.inventory):
        #             cell_surface = pygame.Surface((self.grid_size_x, self.grid_size_y), pygame.SRCALPHA)
        #             cell_rect = pygame.Rect(self.rect_items.x + col * self.grid_size_x, self.rect_items.y + row * self.grid_size_y, self.grid_size_x, self.grid_size_y)
        #             cell_center = (0,0)
        #             cell_surface.blit(self.inventory[fill], cell_center)
        #             self.display_surface.blit(cell_surface, cell_rect)
        #             fill+=1
        #         else:
        #             flag_end=True
        #             break

        pygame.draw.rect(self.display_surface, "black", self.rect_player)
        # image = pygame.image.load("graphics\player\down\down_0.png").convert_alpha()
        # image = pygame.transform.scale(image, ((int(16 * 4), int(16 * 4))))
        # inner_rect_player = pygame.Rect(WIDTH/2 + WIDTH/16, HEIGHT/4 + HEIGHT/16, WIDTH/8, HEIGHT/4)
        # pygame.draw.rect(self.display_surface, "white", inner_rect_player, 3)
        # center_x = inner_rect_player.centerx
        # center_y = inner_rect_player.centery

        # # Get the rectangular area of the image
        # image_rect = image.get_rect()

        # # Set the center of the image to be the same as the center of the inner rectangle
        # image_rect.center = (center_x, center_y)

        # # Blit the image onto the display surface
        # self.display_surface.blit(image, image_rect)

        # for x in range(self.rect_player.x, self.rect_player.x + WIDTH//4, self.grid_size_x):
        #     pygame.draw.line(self.display_surface, "white", (x, self.rect_player.y+self.grid_size_y*3), (x, self.rect_player.y + HEIGHT/2), 3)

        # for y in range(self.rect_player.y+self.grid_size_y*3, self.rect_player.y + self.grid_size_y*4, self.grid_size_y):
        #     pygame.draw.line(self.display_surface, "white", (self.rect_player.x, y), (self.rect_player.x+WIDTH/4, y), 3)
        
        # name = my_font.render('Tiki', False, "white")
        # name_rect = name.get_rect(center = (self.rect_player.centerx,self.rect_player.top+15))
        # self.display_surface.blit(name,name_rect)
        
        # num_cols_hotbar = self.rect_items.width // self.grid_size_x
        # index_num=1
        # for col in range(num_cols_hotbar):
        #     cell_surface = pygame.Surface((self.grid_size_x, self.grid_size_y), pygame.SRCALPHA)
        #     cell_rect = pygame.Rect(self.rect_player.x + col * self.grid_size_x, self.rect_player.y+HEIGHT/3, self.grid_size_x, self.grid_size_y)
        #     index = my_font.render(f'{index_num}', False, "white")
        #     index_rect = name.get_rect(center = (cell_rect.right,cell_rect.bottom))
        #     self.display_surface.blit(index,index_rect)
        #     index_num+=1

        #self.display_surface.blit(image, (inner_rect_player.x, inner_rect_player.y))
    