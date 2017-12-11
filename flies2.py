import sys
import pygame
import dimensions as dm

pygame.init()
screen = pygame.display.set_mode((1000,650))
mouse = pygame.mouse.get_pos()

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Pair(new_x, new_y)

class Hand:
    def __init__(self):
        self.image = pygame.image.load("hand.png").convert_alpha()
        self.position = Pair(mouse[0], mouse[1])
        self.speed = 50
        self.hitbox = pygame.Rect(self.position.x, self.position.y, dm.hand_width, dm.hand_height)
    def display(self, x_pos, y_pos):
        screen.blit(self.image, (x_pos-(dm.hand_width/2), y_pos-(dm.hand_height/2)))

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

"""class flybaby:
    def __init__(self,velocity):
        self.image = pygame.image.load("flybaby.png").convert_alpha()
        self.velocity = velocity
        self.hitbox = pygame.Rect(self.position.x, self.position.y, dm.flybaby_width, dm.flybaby_height)
    def move(self, surface):
        self.image.move_ip(self.velocity.x, self.velocity.y)
        if self.image.right > surface.get_width() or self.image.left < 0:
            self.velocity.x = -self.velocity.x
        if self.image.top < 0:
            self.velocity.y = - self.velocity.y
    def display(self):
        screen.blit(self.image, (x_pos-(dm.hand_width/2), y_pos-(dm.hand_height/2)))"""



  #  def move(self):


hand = Hand()
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    BackGround = Background('background_image.png', [0,0])


    screen.fill((0))

    screen.blit(BackGround.image, BackGround.rect)

   # hand.move()
    hand.display(mouse_x, mouse_y)

    pygame.display.update()
