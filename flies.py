import sys
import pygame
import math 

pygame.init()
screen = pygame.display.set_mode((1000,800))
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
        self.hitbox = pygame.Rect(mouse[0], mouse[1], 200, 293)
    def display(self):
        screen.blit(self.image, mouse)
  #  def move(self):

        
hand = Hand()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    screen.fill((0))
    
   # hand.move()
    hand.display()
    
    pygame.display.update()
