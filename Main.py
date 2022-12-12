###############################################################################################
# SOURCES                                                                                     #
# Chris Cozort's Intro to Computer Programming Class Course Files (https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode&ga=1)
# (https://coderslegacy.com/python/pygame)                                                    #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html)                #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/step_08.html)              #
# (https://coderslegacy.com/python/pygame-platformer-game-development/)                       #
# (https://pythonprogramming.net/pygame-start-menu-tutorial/)                                 #
#                                                                                             #
###############################################################################################

#NEED: Death Screen + Slime image as P1

#Global Variables
import pygame
from pygame.locals import *
import sys
import random

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
GREY = (131, 139, 139)
BROWN = (156, 102, 31)
DARKGREEN = (0, 100, 0)
SLIMEGREEN = (0, 201, 87)

platformcolorlist = GREY, BROWN, DARKGREEN, SLIMEGREEN #created a color list for the platforms to use. It will take a random color from this list and use it as the base platform. 

#Global Variables
HEIGHT = 800 #HEIGHT
WIDTH = 800 #WIDTH
ACC = 0.9 #ACCELERATION
FRIC = -0.01 #FRICTION
FPS = 60 #FPS

FramePerSec = pygame.time.Clock() #Clock/FPS. Will be used to modify FPS

#Setting up clock to mesh with the FPS
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #for me, this means a 800x800px Screen for the game
pygame.display.set_caption("Slime Jump") #Names my game "Bouncing Ball" on the white game bar

#Instantiating Classes (Player/Platforms)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40, 40))
        self.surf.fill((SLIMEGREEN))
        self.rect = self.surf.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT))
        self.vel = vec(0,-4)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0

    def move(self): #Movement keys and acceleration
        self.acc = vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()     
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC #How movement is determined + keeping the player in bounds
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH         
        self.rect.midbottom = self.pos

        autobounce = pygame.sprite.spritecollide(self, platforms, False) #Player will constantly "bounce" when comes into contact with a platform.
        if autobounce:
           self.vel.y = -20 
           
class Platform(pygame.sprite.Sprite): #Small moving platforms
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill(random.choice(platformcolorlist)) #selects from the color list above, choosing from various minecraft colors
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10),
                                                 random.randint(0, HEIGHT-250)))
        self.speed = random.randint(-4, 4)
        self.point = True
        self.moving = True

    def move(self): #Movement for the Small moving platforms
        if self.moving:  
            self.rect.move_ip(self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH

def plat_gen(): #Platform generation
    while len(platforms) < 9 :
        width = random.randint(75,300)
        p = Platform()             
        p.rect.center = (random.randint(0, WIDTH - width),
                        random.randint(-50, 0))
        platforms.add(p)
        all_sprites.add(p)

BPLT = Platform() #Naming platform for use (shorthand)
P1 = Player() #Naming player for use (shorthand)

#Base platform
BPLT.surf = pygame.Surface((WIDTH, 20)) 
BPLT.surf.fill((random.choice(platformcolorlist)))
BPLT.rect = BPLT.surf.get_rect(center = (WIDTH / 2, HEIGHT - 15))

#Sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(BPLT)
all_sprites.add(P1)

#Platforms
platforms = pygame.sprite.Group()
platforms.add(BPLT)

#Platform gen to ensure there will always be an acceptable amount
for x in range(random.randint(7, 9)): #Integer between these two values
    pl = Platform()
    platforms.add(pl)
    all_sprites.add(pl)
    value = 0

#Image loading
image = pygame.image.load("Minecraft_Sunrise.png").convert() #Placed outside loop to prevent loading repeatedly
startingscreen = pygame.image.load("Slime_Jump_Starting_Screen1.png").convert() #Placed outside loop to prevent loading repeatedly
start = False

#Platform destruction and game over
#Game loop
while True:
    for event in pygame.event.get(): #Evauluating quit status of program (to see if functionally running)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #Checks if key is pressed. If spacebar is pressed, the game will start.
            if event.key == pygame.K_SPACE:
                start = True
    
    if start:
        if P1.rect.top <= HEIGHT / 3: #If the player is accelrrating past a certain point, the platforms substantially below will cease to exist
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill() #Kills platform, enabling player to die if they fall off (or more accuratelt, down off of) the screen. 

        if P1.rect.top > HEIGHT: 
            for entity in all_sprites:
                entity.kill()
                displaysurface.fill((RED))
                pygame.display.update()
                pygame.quit()
                sys.exit()
        
        displaysurface.blit(image, (0, 0)) #Image display
        P1.update()
        plat_gen()
    
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect) #O
            entity.move()   

    else:
        displaysurface.blit(startingscreen, (0, 0)) #Starting Screen with instructions is active. 

    pygame.display.update() #updates display
    FramePerSec.tick(FPS) #ensures FPS is consistent 