import pygame
from settings import *
from support import *

class Dialog:
    def __init__(self, scroll_index, text=None):
        self.display_surface = pygame.display.get_surface()
        self.image_dialogbox = my_load("graphics\Dialog\DialogBoxFaceset.png").convert_alpha()
        self.height = self.image_dialogbox.get_height()
        self.image_faceset = my_load("graphics\player\Faceset.png").convert_alpha()
        self.text = text
        self.font = pygame.font.Font('font\Pixeltype.ttf', 25)
        self.chopped = chop_text(self.text)
        self.scroll_index=scroll_index

    def set_text(self,text):
        self.text=text
        self.chopped = chop_text(self.text)
    def set_scroll_index(self,scroll_index):
        self.scroll_index = scroll_index

    def get_rows_in_text_box(self):
        return len(self.chopped)

    def display(self):
        self.display_surface.blit(self.image_dialogbox, (0, HEIGHT-self.height))
        self.display_surface.blit(self.image_faceset, (10, HEIGHT-self.height+30))
        # while True:
        heights = [30,50,70]
        for i in range(3):
            try:
                img = self.font.render(self.chopped[i+self.scroll_index[0]*3], True, 'black')
                self.display_surface.blit(img, (110, HEIGHT-self.height+heights[i]+7))
            except:
                pass
        

def chop_text(text):
    MAX_LENGTH = 55
    chopped_text = {}
    space_index =0
    index=0
    while text:
        if len(text) <= MAX_LENGTH:
            chopped_text[index] = text
            text = text[space_index+1:]
            index+=1
            break
        else:
            chunk = text[:MAX_LENGTH]
            space_index = chunk.rfind(',')
            if space_index == -1:
                space_index = MAX_LENGTH
            chopped_text[index] = text[:space_index+1]
            text = text[space_index+1:]
            index+=1
        

    return chopped_text
    