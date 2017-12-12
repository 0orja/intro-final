import sys
import pygame
import random
"""DIMENSIONS"""
hand = {
"width": 85,
"height": 124,
"img": "hand.png"}

pizza = {
"width": 170,
"height": 100,
"img": "pizza.png"}

fly_dm = {
"width": 44,
"height": 41,
}

gun_dm = {
"width": 138,
"height": 141
}
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
h = screen.get_height()
w = screen.get_width()
mouse_x, mouse_y = pygame.mouse.get_pos()
pygame.init()
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Pair(new_x, new_y)
class PizzaGuy:
    def __init__(self):
        self.image = pygame.image.load("hand.png").convert_alpha()
        self.position = Pair(mouse[0], mouse[1])
        self.dimensions = Pair(dm.hand["width"], dm.hand["height"])
        self.hitbox = pygame.Rect(self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
    def display(self, x_pos, y_pos):
        screen.blit(self.image, (x_pos-(dm.hand["width"]/2), y_pos-(dm.hand["height"]/2)))
        pygame.draw.rect(screen, (255,255,255), self.hitbox)
    def move(self):
        self.position = Pair(mouse_x, mouse_y)
class Gun: 
    def __init__(self):
        self.sheet = [pygame.image.load("gun-1.png"),pygame.image.load("gun-2.png")]
        self.ani_pos = 0
        self.image = self.sheet[self.ani_pos]
        self.position = Pair(mouse_x, mouse_y)
        self.ani_speed = 10
        self.hitbox = pygame.Rect(self.position.x, self.position.y, gun_dm["width"], gun_dm["height"])
    def update(self):
        self.position = Pair(pygame.mouse.get_pos()[0], pygame.mouse.get_pos[1])
    def idle(self, x, y):
        self.image = self.sheet[0]
        screen.blit(self.image, (x-(gun_dm["width"]/2), y-(gun_dm["height"]/2)))
        print("no")
    def shoot(self, x, y):
        #self.ani_speed -= 5
        #if self.ani_speed == 0:
        self.ani_speed -= 1
        while self.ani_speed:
            self.image = self.sheet[1] #
            screen.blit(self.image, (x-(gun_dm["width"]/2), y-(gun_dm["height"]/2)))
        self.idle(x, y)
        print("yes")
    def display(self, x, y, status):
        self.status = status
        if self.status == "shoot":
            self.image = self.sheet[1]
            screen.blit(self.image, (x-(gun_dm["width"]/2), y-(gun_dm["height"]/2)))
        if self.status == "idle":
            self.image = self.sheet[0]
            screen.blit(self.image, (x-(gun_dm["width"]/2), y-(gun_dm["height"]/2)))


class Fly:
    def __init__(self):
        self.sheet = [pygame.image.load("fly-1.png"), pygame.image.load("fly-2.png"), pygame.image.load("fly-3.png"), pygame.image.load("fly-4.png")]
        self.dead = pygame.image.load("fly-dead.png")
        self.ani_pos = 0
        self.image = self.sheet[self.ani_pos]
        self.ani_speed = 5
        self.position = Pair(random.randint(0,w), random.randint(0,h))
        self.velocity = Pair(random.randint(1,5), random.randint(1,5))
        self.dimensions = Pair(fly_dm["width"], fly_dm["height"])
        self.hitbox = pygame.Rect(self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
    def display(self):
        screen.blit(self.image, self.hitbox.topleft)
    def move(self):
        self.position += self.velocity
        self.hitbox.move_ip(self.velocity.x, self.velocity.y)
        if self.hitbox.right > w or self.hitbox.left < 0:
            self.velocity.x = -self.velocity.x
        if self.hitbox.top < 0 or self.hitbox.bottom > h:
            self.velocity.y = - self.velocity.y
        self.ani_speed -= 1
        if self.ani_speed == 0:
            if self.ani_pos < 4:
                self.image = self.sheet[self.ani_pos]
                self.ani_pos += 1
            else:
                self.ani_pos = 0
            self.ani_speed = 10
        screen.blit(self.image, self.hitbox.topleft)
    def die(self):
        self.image = self.dead
class Background(pygame.sprite.Sprite): #make backgrounds blurred or darker
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        screen.blit(self.image, self.rect)
f = Fly()
gun = Gun()

while True:
    screen.fill((0))
    clock.tick(60)
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gun.display(x, y, "shoot")
#        event.type == pygame.MOUSEBUTTONUP:
#            gun.idle(x, y)
    #marketplace = Background("marketplace.png", [0,0])
#    click = pygame.mouse.get_pressed()
#    if click[0]:
    gun.display(x, y, "idle")


   # hand.move()
    #gun.shoot(x, y)
    f.display()
    f.move()

    pygame.display.update()
