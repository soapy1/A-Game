#TODO: fix movement of computer

#!/usr/bin/env python2

'''a module for sprites using pygame '''

import pygame, os, random
from pygame import sprite

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

        self.image = pygame.image.load('game/data/grossini.png').convert()
        self.rect = self.image.get_rect()

pygame.init()

# Set the dimensions of the screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

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
x_co = screen_width/2
y_co = screen_height/2

car.rect.x = x_co
car.rect.y = y_co

# Coordinates for charTwo
person.rect.x = random.randint(0,1000) 
person.rect.y = random.randint(0,700)

# Key repeating
pygame.key.set_repeat(5,10)

# Manages how fast the screen updates
clock = pygame.time.Clock()

# Main Program Loop
while not done:  
    screen.fill(black)
    all_list.draw(screen)
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
            elif event.key == pygame . K_RIGHT :
                car.rect.x += 25
            elif event.key == pygame . K_UP :
                car.rect.y -= 25
            elif event.key == pygame . K_DOWN :
                car.rect.y += 25

    # TODO: Fix this to make sprite move better
    # Randomly moves sprite 'person'
    place = random.randint(0,3)
    if place == 0:
        person.rect.x += 25
    if place == 1:
        person.rect.x -= 25
    if place == 2:
       person.rect.y += 25
    if place == 3:
       person.rect.y -= 25

pygame.quit()
