import pygame
from settings import *
from support import *
import dialog
import math

class Journal:
    def __init__(self, scroll_index, current_quest):
        self.display_surface = pygame.display.get_surface()
        self.quest1 = '''Quest: Wind potion for Emily. 
        ~Dear Tiki, I've heard about your potionmaking talent, please create 1 wind potion for me.'''
        self.quest2 = '''Quest: Shining potion for Wendy. 
        ~Dear Tiki, The nights are getting dark and scary, I just can't sleep, please create 1 shining potion for me.'''
        self.quest3 = '''Quest: Fire potion for King Arthur. 
        ~Dear mighty forest witch, please create 1 fire potion for me so that I can destroy my enemies.'''
        self.quests = {1:self.quest1, 2: self.quest2, 3: self.quest3}
        self.current_quest = current_quest
        self.dialog = dialog.Dialog(self.quests[self.current_quest], f"Quest {self.current_quest}", delimiter=' ')
        self.scroll_index=scroll_index
        self.max_length= self.dialog.get_rows_in_text_box()
    def update_journal(self, new_scroll_index):
        self.current_text = f"Quest {self.current_quest}"
        self.dialog.set_text(self.quests[self.current_quest], self.current_text)
        self.dialog.set_scroll_index(new_scroll_index)
        self.scroll_index=new_scroll_index
        self.max_length= math.ceil(self.dialog.get_rows_in_text_box()/3)
    def change_quest(self, new_quest):
        self.current_quest = new_quest
        self.current_text = f"Quest {self.current_quest}"
        self.dialog.set_text(self.quests[self.current_quest], self.current_text)
    def display(self):
        self.dialog.display()
    