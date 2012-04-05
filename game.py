#TODO: fix movement of computer
#      Fix movement of character and make it move on map

#!/usr/bin/env python2

'''a module for sprites using pygame '''

import pygame, os, random
from pygame import sprite
from game import maps
from xml.etree import ElementTree as etree

white = (255,255,255)
black = (0,0,0)

class charCar (pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('game/data/car.png').convert()
        self.rect = self.image.get_rect()

class charTwo (pygame.sprite.Sprite):        

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('game/data/tree2-final.png').convert()
        self.rect = self.image.get_rect()

pygame.init()

# Sets up the screen
scr = pygame.display.set_mode()
m = maps.Map('one.tmx')
# Draw to temporary surface.
s = pygame.Surface((m.height*m.tileheight, m.width*m.tilewidth))
m.draw(s)

# Create a sprite list that will be drawn to the screen
all_list = pygame.sprite.RenderPlain()
sprite_list = pygame.sprite.RenderPlain()

# Create the sprite 'car' and 'person'
car = charCar (black, 20, 15)
person = charTwo (black, 20, 15)
# Add sprite car and person to the sprite lists
all_list.add(car)
sprite_list.add(person)
all_list.add(person)

done = False

# Default coordinates for the sprite
x_co = 50
y_co = 50

car.rect.x = x_co
car.rect.y = y_co

# Coordinates for charTwo
person.rect.x = random.randint(0,1000) 
person.rect.y = random.randint(0,700)

# Key repeating
pygame.key.set_repeat(10,100)

# Manages how fast the screen updates
clock = pygame.time.Clock()

x_offset = 0; y_offset = 0
min_x = scr.get_width()-s.get_width()
min_y = scr.get_height()-s.get_height()

# Main Program Loop
while not done: 
    scr.blit(s, (x_offset, y_offset))
    all_list.draw(scr)
    clock.tick(60)
    pygame.display.flip()

    # Detect collisions of the sprite 'car' 
    hit_list = sprite.spritecollide(car, sprite_list, True)
    if len (hit_list) > 0:
        done = True 

    for event in pygame.event.get():
        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
	# Controls for the car
            if event.key == pygame.K_q:
                done = True 
            elif event.key == pygame. K_LEFT :
                car.rect.x -= 25
                x_offset += 25
                if x_offset < min_x: x_offset=min_x
            elif event.key == pygame . K_RIGHT :
                car.rect.x += 25
                x_offset -= 25
                if x_offset > 0: x_offset=0
            elif event.key == pygame . K_UP :
                car.rect.y -= 25
                y_offset += 25
                if y_offset < min_y: y_offset=min_y
            elif event.key == pygame . K_DOWN :
                car.rect.y += 25
                y_offset -=25
                if x_offset > 0: x_offset=0

    # Moves the sprite 'person' around randomly
    # TODO: Make this work better
    num = random.randint(0,3)
    if num == 0:
        dis = random.randint(0,100)
        person.rect.x -= dis
    elif num == 1:
       dis = random.randint(0,100)
       person.rect.x += dis
    elif num == 2:
        dis = random.randint(0,100)
        person.rect.y += dis
    elif num == 3:
        dis = random.randint(0,100)
        person.rect.y -= dis

pygame.quit()
