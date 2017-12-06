import pygame
import dimensions as dm
import random
import images

screen = pygame.display.set_mode((800,600))
mouse = pygame.mouse.get_pos()
h = screen.get_height()
w = screen.get_width()

pygame.init()
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
        self.dimensions = Pair(dm.hand["width"], dm.hand["height"])
        self.hitbox = pygame.Rect(self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
    def display(self, x_pos, y_pos):
        screen.blit(self.image, (x_pos-(dm.hand["width"]/2), y_pos-(dm.hand["height"]/2)))
#        pygame.draw.rect(screen, (255,255,255), self.hitbox)
#    def move():
#        self.position = Pair
class Food:
    def __init__(self, foodtype):
        self.foodtype = foodtype
        self.image = pygame.image.load("pizza.png").convert_alpha() #how to store "foodtype" attribute such that it can be used here?
        self.position = Pair(random.randint(0,w), random.randint(0,h))
        self.dimensions = Pair(dm.pizza["width"], dm.pizza["height"])
        self.hitbox = pygame.Rect(self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
    def display(self):
        screen.blit(self.image, (self.position.x, self.position.y))

        #screen.blit(self.hitbox, (self.position.x, self.position.y))
class Fly:
    def __init__(self):
        self.image = pygame.image.load("flybaby.png").convert_alpha()
        self.position = Pair(random.randint(0,w), random.randint(0,h))
        self.velocity = Pair(random.randint(1,10), random.randint(1,10))
        self.dimensions = Pair(dm.fly["width"], dm.fly["height"])
        self.hitbox = pygame.Rect(self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
    def display(self):
        screen.blit(self.image, (self.position.x, self.position.y))
    def move(self):
        self.position += self.velocity
        self.hitbox.move_ip(self.velocity.x, self.velocity.y)
        if self.hitbox.right > w or self.hitbox.left < 0:
            self.velocity.x = -self.velocity.x
        if self.hitbox.top < 0 or self.hitbox.bottom > h:
            self.velocity.y = - self.velocity.y
