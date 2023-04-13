import pygame
from settings import *
from support import *
import dialog
import math

class Inventory_menu:
    def __init__(self, scroll_index, inventory=None):
        self.display_surface = pygame.display.get_surface()
        self.inventory = inventory
        self.dialog = dialog.Dialog(f"Let's see what I have...: {self.inventory}")
        self.scroll_index=scroll_index
        self.max_length= self.dialog.get_rows_in_text_box()
    def update_inventory(self, new_inventory, new_scroll_index):
        self.inventory = new_inventory
        self.dialog.set_text(f"Let's see what I have...: {self.inventory}")
        self.dialog.set_scroll_index(new_scroll_index)
        self.scroll_index=new_scroll_index
        self.max_length= math.ceil(self.dialog.get_rows_in_text_box()/3)
    def display(self):
        if self.scroll_index[0]>=self.max_length:
            self.scroll_index[0]=0
        self.dialog.display()
    