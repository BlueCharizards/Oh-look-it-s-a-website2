import pygame
import random

WIDTH = 600 #width of our game window
HEIGHT = 480 #height of our game window
FPS = 60

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (115, 0, 195)
PINK = (205, 0, 102)
light_blue = (65, 105, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(light_blue)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
    def update(self):
        self.rect.y += 10
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

#Initialize and create game window

pygame.init()
pygame.mixer.init() #initializes sound
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #create screen
pygame.display.set_caption("Game") #give game a name
clock = pygame.time.Clock() #keep track of speed/time

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


#Game Loop
running = True
while running:
    clock.tick(FPS) #keep the loop running at the right speed
    #Process Inputs (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    #Updates
    all_sprites.update()
    #Renders (draws)
    screen.fill(PURPLE)
    all_sprites.draw(screen)
    #after drawing everything, flip the display
    pygame.display.flip()
pygame.quit()

