import pygame
import sys
screen = pygame.display.set_mode((800,600))
pygame.init()
font = pygame.font.Font("malgunbd.ttf", 48)
while 1:
    screen.fill((0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    text = font.render("hello", True, (255,255,255))
    screen.blit(text, (100,100))

    pygame.display.update()
    
