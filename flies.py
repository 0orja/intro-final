import sys
import pygame
import dimensions as dm
import classes

pygame.init()
screen = classes.screen
mouse = pygame.mouse.get_pos()

hand = classes.Hand()
pizza = classes.Food("pizza.png")
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    screen.fill((0))

   # hand.move()
    hand.display(mouse_x, mouse_y)
    pizza.display()

    pygame.display.update()
