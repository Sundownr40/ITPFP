###############################################################################################
# SOURCES                                                                                     #
# (https://coderslegacy.com/python/pygame)                                                    #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html)                #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/step_08.html)              #
# (https://coderslegacy.com/python/pygame-platformer-game-development/)                       #
# (https://pythonprogramming.net/pygame-start-menu-tutorial/)                                 #
#                                                                                             #
###############################################################################################

#I want 
#Starting Screen
#Proper platform generation
#Background image

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

#Global Variables
HEIGHT = 800 #HEIGHT
WIDTH = 400 #WIDTH
ACC = 0.5 #ACCELERATION
FRIC = -0.01 #FRICTION
FPS = 60 #FPS

FramePerSec = pygame.time.Clock() #Clock/FPS. Will be used to modify FPS

#Setting up clock to mesh with the FPS
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #for me, this means a 400x450px Screen for the game
pygame.display.set_caption("Bouncing Ball") #Names my game "Bouncing Ball" on the white game bar

#Instantiating Classes (Player/Platforms)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((RED))
        self.rect = self.surf.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT))
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

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH         
        self.rect.midbottom = self.pos

        autobounce = pygame.sprite.spritecollide(self, platforms, False)
        if autobounce:
           self.vel.y = -15 

class startingplatform(pygame.sprite.Sprite): #Starting platform
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(((50,100)))
        self.surf.fill((WHITE))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-250)))


class platform(pygame.sprite.Sprite): #Small moving platforms
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((BLUE))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-250)))
        self.speed = random.randint(-2, 2)
        self.point = True   
        self.moving = True

    def move(self): #Movement for the Small moving platforms
        if self.moving == True:  
            self.rect.move_ip(self.speed,0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH

def plat_gen(): #Platform generation
    while len(platforms) < 9 :
        width = random.randrange(75,125)
        p = platform()             
        p.rect.center = (random.randrange(0, WIDTH - width),
                        random.randrange(-50, 0))
        platforms.add(p)
        all_sprites.add(p)

BPLT = platform()
P1 = Player()

BPLT.surf = pygame.Surface((WIDTH, 20))
BPLT.surf.fill((WHITE))
BPLT.rect = BPLT.surf.get_rect(center = (WIDTH/2, HEIGHT-15))

all_sprites = pygame.sprite.Group()
all_sprites.add(BPLT)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(BPLT)

for x in range(random.randint(7, 9)):
    pl = platform()
    platforms.add(pl)
    all_sprites.add(pl)
    value = 0

variableforfirstplatform = 0

#Platform destruction and game over
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            displaysurface.fill((RED))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()
         
    displaysurface.fill((BLACK)) #This is where I will input a background image
    P1.update()
    plat_gen()
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
 
    pygame.display.update()
    FramePerSec.tick(FPS)