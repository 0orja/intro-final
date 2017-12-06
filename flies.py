import sys
import pygame
import dimensions as dm
import classes

pygame.init()


hand = classes.Hand()
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    classes.screen.fill((0))

   # hand.move()
    hand.display(mouse_x, mouse_y)

    pygame.display.update()
