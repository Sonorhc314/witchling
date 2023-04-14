import pygame
from settings import *
from support import *
import dialog
import math

class Inventory_menu:
    def __init__(self, scroll_index, inventory=None):
        self.display_surface = pygame.display.get_surface()
        self.inventory = inventory
        self.inventory_to_text()
        self.dialog = dialog.Dialog(f"Let's see what I have...: {self.inventory_text}", "Tiki")
        self.scroll_index=scroll_index
        self.max_length= self.dialog.get_rows_in_text_box()
    def update_inventory(self, new_inventory, new_scroll_index):
        self.inventory = new_inventory
        self.inventory_to_text()
        self.dialog.set_text(f"Let's see what I have...: {self.inventory_text}")
        self.dialog.set_scroll_index(new_scroll_index)
        self.scroll_index=new_scroll_index
        self.max_length= math.ceil(self.dialog.get_rows_in_text_box()/3)
    def inventory_to_text(self):
        self.inventory_text = ''
        if self.inventory is None or len(self.inventory)==0:
            self.inventory_text+=' Nothing yet!'
        elif self.inventory is not None:
            for key in self.inventory:
                self.inventory_text+=f' {key}: {self.inventory[key]},'
            self.inventory_text = self.inventory_text[:-1]
        return self.inventory_text
    def display(self):
        if self.scroll_index[0]>=self.max_length:
            self.scroll_index[0]=0
        self.dialog.display()
    