import pygame
import sys

pygame.init()
surface = pygame.display.set_mode((800,600))
mouse = pygame.mouse.get_pos()
#blank = pygame.draw.circle(surface,) ######################## here
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Pair(new_x, new_y)

class Particle:
    def __init__(self, rect, velocity):
        self.rect = rect
        self.velocity = velocity
    def move(self, surface):
        self.rect.move_ip(self.velocity.x, self.velocity.y)

        if self.rect.right > surface.get_width() or self.rect.left < 0:
            self.velocity.x = -self.velocity.x
        if self.rect.top < 0:
            self.velocity.y = - self.velocity.y
    def display(self):
        pygame.draw.rect(surface, (255,255,255), self.rect)

a = pygame.Rect(100,100,10,10)
p = Particle(a, Pair(1,1))
particles = [p]
b = pygame.Rect(400,550,100,10)

counter = 0
font = pygame.font.Font(None, 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            r = pygame.Rect(click, (10,10))
            p2 = Particle(r, Pair(1, 1))
            particles.append(p2)
    surface.fill((0, 0, 0))
    # paddle
    text = font.render(str(counter), True, (255, 255, 255))
    surface.blit(text, (100, 100))

    pygame.draw.rect(surface, (255,0,0), b)
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        b.move_ip(1,0)
    if key[pygame.K_LEFT]:
        b.move_ip(-1,0)
    """
    pygame.event.get()
    click = pygame.mouse.get_pressed()
    if click[0]:
            r = pygame.Rect(mouse[0], mouse[1], 10,10)
            p2 = Particle(r, a_vel)
            particles.append(p2) """
    for p in particles:
        p.display()
        p.move(surface)
        if p.rect.colliderect(b):
            p.velocity.y = - p.velocity.y
            counter += 1

#        if p.rect.bottom > surface.get_height():
#            particles.remove(p)
    #tmplist = []
    #for p in particles:
        # is particle out of screen?
    #particles = tmplist

    if not particles:
        pygame.display.quit()
        sys.exit()
    pygame.display.update()
