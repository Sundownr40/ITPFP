###############################################################################################
# SOURCES                                                                                     #
# (https://coderslegacy.com/python/pygame)                                                    #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html)                #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/step_08.html)              #
# (https://coderslegacy.com/python/pygame-platformer-game-development/)                       #
# (https://pythonprogramming.net/pygame-start-menu-tutorial/)                                 #
#                                                                                             #
###############################################################################################

#Global Variables
import pygame
from pygame.locals import *
import sys
import random
import time

#Initialize Pygame
pygame.init() 

vec = pygame.math.Vector2 #2-Dimensional vectors (Vector2)
#Colors. I like having a large variety 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,211,67)
ORANGE = (255,128,0)
PURPLE = (106, 13, 173)
PINK = (243, 58, 106)
#
#

HEIGHT = 450 #HEIGHT
WIDTH = 400 #WIDTH
ACC = 0.5 #ACCELERATION
FRIC = -0.01 #FRICTION
FPS = 60 #FPS

FramePerSec = pygame.time.Clock() #Clock/FPS. Will be used to modify FPS
#Setting up clock to mesh with the FPS
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #for me, this means a 400x450px Screen for the game
pygame.display.set_caption("Bouncing Ball") #Names my game "Bouncing Ball" on the white game bar

#Instantiating Classes (Player/Platforms)














#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((RED))
        self.rect = self.surf.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT/1.2))
        self.vel = vec(0,-4)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC

        doublejump = pygame.sprite.spritecollide(self, platforms, False)
        if doublejump:
           self.vel.y = -15 

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH         
        self.rect.midbottom = self.pos













#Platforms
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((WHITE)) #Will be WHITE temporarally
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

BPLT = platform() #Starting Platform Player will come to rest on
P1 = Player() #Player