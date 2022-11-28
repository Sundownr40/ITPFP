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

#Setting up Constants
HEIGHT = 450 #HEIGHT
WIDTH = 400 #WIDTH
ACC = 1 #ACCELERATION
FRIC = -0.10 #FRICTION
FPS = 60 #FPS

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

