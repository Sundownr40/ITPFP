###############################################################################################
# SOURCES                                                                                     #
# Chris Cozort's Intro to Computer Programming Class Course Files (https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode&ga=1)
# (https://coderslegacy.com/python/pygame)                                                    #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html)                #
# (https://api.arcade.academy/en/latest/examples/platform_tutorial/step_08.html)              #
# (https://coderslegacy.com/python/pygame-platformer-game-development/)                       #
# (https://pythonprogramming.net/pygame-start-menu-tutorial/)                                 #
# Ryan Deivert '23 - Special thanks for assistance in my platform generation errors           #
#                                                                                             #
###############################################################################################

#Global Variables
import pygame
from pygame.locals import *
import sys
import random
pygame.init() #Initializes pygame, the API I am using for the game

#Utilizing 2-Dimensional vectors (Vector2). It is easier to store information in a vector as opposed to 2 seperate cordinates. Higher functionality
vec = pygame.math.Vector2 

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
TANGREEN = (139, 139, 0)
YELLOWGREEN = (205, 205, 0)

#Created a color tuple for the platforms to use
#It will take a random color and use it as the base platform
platformcolortuple = GREY, BROWN, DARKGREEN, SLIMEGREEN, TANGREEN, YELLOWGREEN

#Global Variables
HEIGHT = 800 #HEIGHT
WIDTH = 800 #WIDTH
ACC = 0.5 #ACCELERATION
FRIC = -0.05 #FRICTION
FPS = 60 #FRAMES PER SECOND

#Clock/FPS. Will be used to modify FPS
FramePerSec = pygame.time.Clock()

#Setting up clock to mesh with the FPS
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #In "Slime Jump's" case, this means a 800x800px Screen for the game
pygame.display.set_caption("Slime Jump") #Names my game "Slime Jump" on the white game bar (window)

#Instantiating Classes (Player/Platforms)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load("Slime_P1.png").convert()
        self.rect = self.surf.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT))
        self.vel = vec(0,-4)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0

    #Dead status 
    def dead(self): 
       return self.rect.top > HEIGHT

    #Movement dynamics 
    def move(self): #Movement keys, variables and acceleration
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

        #Bounce when Slime hits platform
        autobounce = pygame.sprite.spritecollide(self, platforms, False) 
        if autobounce:
           self.vel.y = -20
        
class Platform(pygame.sprite.Sprite): #Small moving platforms
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,200), 12))
        self.surf.fill(random.choice(platformcolortuple)) #selects from the color tuple above, choosing from various minecraft colors
        self.rect = self.surf.get_rect(center = (random.randint(0, WIDTH-10), #Set platform to random position
                                                 random.randint(0, HEIGHT-250)))
        self.speed = random.randint(-4, 4)
        self.point = True
        self.moving = True

    def move(self): #Off-screen switch sides
        if self.moving:  
            self.rect.move_ip(self.speed, 0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH

def plat_gen(): #Platform generation
    while len(platforms) < 8:
        width = random.randint(75, 300)
        p = Platform()             
        p.rect.center = (random.randint(0, WIDTH - width),
                        random.randint(-60, 0))
        platforms.add(p)
        all_sprites.add(p)

BPLT = Platform() #Instantiating platforms
P1 = Player() #Instantiting a player 

#Base platform
BPLT.surf = pygame.Surface((WIDTH * 2, 20)) 
BPLT.surf.fill((random.choice(platformcolortuple)))
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
background = pygame.image.load("Minecraft_Sunrise.png").convert() #Placed outside loop to prevent loading repeatedly
startingscreen = pygame.image.load("Slime_Jump_Starting_Screen1.png").convert() #Placed outside loop to prevent loading repeatedly
deathscreen = pygame.image.load("You_Died_Updated.png").convert() #Death screen placed outside loop to prevent loading issues
start = False

deathtimer = 3000 #upon death, the death screen will appear for 3 second before the program exits. 

#Platform destruction and game over
#Game loop
while True:
    isdead = P1.dead()
    for event in pygame.event.get(): #Evauluating quit status of program (to see if functionally running)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #Checks if key is pressed. If spacebar is pressed, the game will start
            if event.key == pygame.K_ESCAPE: #Esc = exit game
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE: #Clicking space begins the game from the home screen
                start = True

    if start: #If space is pressed...
        if P1.rect.top <= HEIGHT / 3: #If the player is accelerating past a certain point, the platforms substantially below will cease to exist
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill() #Kills platform, enabling player to die if they fall off (or more accurately, down off of) the screen
        
        displaysurface.blit(background, (0, 0)) #Image display of background
        if not isdead:
            P1.update() #since 60fps, it will update every 60th of a second
        plat_gen()
    
        for entity in all_sprites: #Iterates through all_sprites
            displaysurface.blit(entity.surf, entity.rect)
            entity.move() #calls move method for all objects in "all_sprites" list

    else: #if space has not been pressed...
        displaysurface.blit(startingscreen, (0, 0)) #Starting Screen with instructions is active. 
    if isdead: #if P1 dies...
        pygame.time.wait(500) #waits for a 1/2 second before death screen to allow player to comprehend their death
        displaysurface.blit(deathscreen, (0, 0))
        deathtimer -= FramePerSec.get_time()
        if deathtimer <= 0:
            pygame.quit()
            sys.exit()

    pygame.display.update() #updates display
    FramePerSec.tick(FPS) #ensures FPS is consistent 