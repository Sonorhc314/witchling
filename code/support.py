from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list=[]

    for _,__,img_folder in walk(path):
        for image in img_folder:
            full_path = path + '\\' + image
            image_surface = my_load(full_path).convert_alpha() 
            surface_list.append(image_surface)

    return surface_list

def my_load(path):
    image_surface = pygame.transform.scale_by(pygame.image.load(path), 2)
    return image_surface