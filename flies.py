import sys
import pygame
import dimensions as dm
import classes

pygame.init()
screen = classes.screen
mouse = pygame.mouse.get_pos()

hand = classes.Hand()
pizza = classes.Food("pizza.png")
f = classes.Fly()
while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    screen.fill((0))

   # hand.move()
    hand.display(mouse_x, mouse_y)
    hand.position = classes.Pair(mouse_x, mouse_y)
    pizza.display()
    f.display()
    f.move()
#    if f.hitbox.colliderect(hand.hitbox):
#        f.velocity.x = -f.velocity.x
#        f.velocity.y = -f.velocity.y

    pygame.display.update()
