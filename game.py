#TODO: fix movement (allow for rotation when moving car) 

#!/usr/bin/env python2

'''a module for sprites using pygame '''

import pygame, os, random
from pygame import sprite
from game import maps

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

# Initializes the mixer for music
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

# Sets up the screen
pygame.display.set_caption('GET THAT TREE!')
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

# Coordinates for the sprite
car_x = scr.get_width()/2 
car_y = scr.get_height()/2

car.rect.x = car_x
car.rect.y = car_y

# Coordinates for charTwo
person_x = random.randint(0, 2400)
person_y = random.randint(0, 2400)

person.rect.x = person_x 
person.rect.y = person_y

# Key repeating
pygame.key.set_repeat(100,5)

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
    
    # Plays poorly recorded music 
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.load('game/data/walking_around_theme.ogg')
        pygame.mixer.music.play()

    for event in pygame.event.get():
        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
	# Controls for the car
            if event.key == pygame.K_q:
                pygame.mixer.music.stop()
                done = True 
            elif event.key == pygame. K_LEFT :
                x_offset += 25
                if x_offset < min_x: x_offset=min_x
            elif event.key == pygame . K_RIGHT :
                x_offset -= 25
                if x_offset > 0: x_offset=0
            elif event.key == pygame . K_UP :
                y_offset += 25
                if y_offset < min_y: y_offset=min_y
            elif event.key == pygame . K_DOWN :
                y_offset -=25
                if x_offset > 0: x_offset=0

    # Moves the sprite 'person' around randomly
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

    # Makes sure the sprite 'person' does not leave the screen
    if person.rect.x >  2400:
        person.rect.x -= 20
    elif person.rect.x < 0:
        person.rect.x += 20
    elif person.rect.y > 2400:
        person.rect.y -= 20
    elif person.rect.y < 0:
        person.rect.y += 20

pygame.quit()
