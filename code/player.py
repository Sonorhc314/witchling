import pygame
from settings import * 
from support import *
from debug import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites=None, pickup_sprites=None, visible_sprites=None,
                 entrance_sprites=None, portal_sprites=None):
        super().__init__(groups)
        self.image = my_load('graphics\player\down_idle\down_idle.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-5)
        self.direction = pygame.math.Vector2()
        #animations
        self.import_player_assets()
        self.status = 'down'
        #movement
        self.attacking = False
        self.attack_cooldown = 600
        self.attack_time = None
        self.speed = 3
        self.frame_index=0
        self.animation_speed = 0.1
        self.obstacle_sprites = obstacle_sprites  # store the obsta
        self.pickup_sprites = pickup_sprites
        self.visible_sprites = visible_sprites
        #inventory
        self.inventory = {}
        self.picking_up = False
        self.picking_up_time = None
        self.pickup_cooldown = 300
        #self.in_inventory = False
        #self.inventory_cooldown = 300
        # self.inventory_time = None
        #portal
        self.portal_sprites= portal_sprites
        #door
        self.entrance_sprites = entrance_sprites

    def import_player_assets(self):
        character_path = "graphics\player\\"
        self.animations = {'dead':[],'up':[], 'down':[], 'left':[], 'right':[], 
                           'right_idle':[], 'left_idle':[],'up_idle':[],'down_idle':[],
                           'right_attack':[], 'left_attack':[],'up_attack':[],'down_attack':[]}
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(character_path + animation)

    def get_inventory(self):
        return self.inventory

    def input(self):
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y =0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x =0

        #attack
        if keys[pygame.K_SPACE] and not self.attacking:
            self.attacking=True
            self.attack_time = pygame.time.get_ticks()
            #print("attack")
        
        #magic
        if keys[pygame.K_1] and not self.attacking:
            self.attacking=True
            self.attack_time = pygame.time.get_ticks()
            #print("magic")
        #inventory
        # if keys[pygame.K_i] and not self.in_inventory:
        #     self.in_inventory=True
        #     self.inventory_time = pygame.time.get_ticks()
        #     print(self.inventory)

        #pickup
        if keys[pygame.K_e] and not self.picking_up:
            for sprite in self.pickup_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if sprite.get_name() in self.inventory:
                        self.inventory[sprite.get_name()]+=1
                    else:
                        self.inventory[sprite.get_name()] = 1
                    self.picking_up=True
                    self.picking_up_time = pygame.time.get_ticks()
                    pygame.sprite.Sprite.kill(sprite)
        if keys[pygame.K_SPACE]:
            for sprite in self.portal_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    print("portal enetered")
            
    def move(self, speed):
        if self.direction.magnitude()>0:
            self.direction=self.direction.normalize()

        self.hitbox.x += self.direction.x*speed 
        self.collision('horizontal')
        self.hitbox.y += self.direction.y*speed 
        self.collision('vertical')
        self.rect.center = self.hitbox.center
        #self.rect.center += self.direction*speed 

    def teleport(self, destination):
        self.hitbox.x = destination[0]
        self.hitbox.y = destination[1]
        self.rect.center = self.hitbox.center
    
    def update_sprites(self, new_visible, new_entrance, new_obstacle, new_pickup, new_portal=None):
        self.pickup_sprites = new_pickup
        self.obstacle_sprites = new_obstacle
        self.entrance_sprites = new_entrance
        self.portal_sprites = new_portal
        self.visible_sprites = new_visible
        self.groups=self.visible_sprites


    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status += '_idle' 
        if self.attacking:
            self.direction.x =0
            self.direction.y=0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status =  self.status.replace('_idle', '_attack')
                else:
                    self.status += '_attack'
        else:
            self.status = self.status.replace('_attack', '')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking=False
        if self.picking_up:
            if current_time - self.picking_up_time >= self.pickup_cooldown:
                self.picking_up=False

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

        if self.pickup_sprites is not None:
            for sprite in self.pickup_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    debug("Pick up using E")

        if self.portal_sprites is not None:
            for sprite in self.portal_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    debug("Enter portal")
        # if self.entrance_sprites is not None:
        #     for sprite in self.entrance_sprites:
        #         if sprite.hitbox.colliderect(self.hitbox):
        #             debug("home")

    def collision_item(self):
        pass
        # for sprite in self.obstacle_sprites:
        #     if sprite.hitbox.colliderect(self.hitbox):
        #         debug("a")
        #         self.inventory.append(len(self.inventory))

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)