import pygame
import sys
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.init()
while 1:
    screen.fill((0))
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    mouse_status = pygame.mouse.get_pressed()
    if mouse_status[0]:
        print("yes")
    else:
        print("no")
    pygame.display.update()
    
