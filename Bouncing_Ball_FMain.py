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
HEIGHT = 450 #HEIGHT
WIDTH = 400 #WIDTH
ACC = 0.5 #ACCELERATION
FRIC = -0.10 #FRICTION
FPS = 60 #FPS
FramePerSec = pygame.time.Clock() #Clock/FPS. Will be used to modify FPS

#Setting up clock to mesh with the FPS
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #for me, this means a 400x450px Screen for the game
pygame.display.set_caption("Bouncing Ball") #Names my game "Bouncing Ball" on the white game bar

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

#Instantiating Classes (Player/Platforms)

#Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30)) #30x30px player
        self.surf.fill((RED)) #Player will be RED temporarally
        self.rect = self.surf.get_rect(center = (10, 420))

#Platforms
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((WHITE)) #Will be WHITE temporarally
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

BASEPLAT1 = platform() #Starting Platform Player will come to rest on
PLY = Player #Player