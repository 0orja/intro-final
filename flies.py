import sys
import pygame
import random
pygame.init()
surface = pygame.display.set_mode((640,480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
