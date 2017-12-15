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
cat_dm = {
"width": 140,
"height": 100
}
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
h = screen.get_height()
w = screen.get_width()
mouse_x, mouse_y = pygame.mouse.get_pos()
miss_sound = pygame.mixer.Sound("miss.wav")
hit_sound = pygame.mixer.Sound("shotgun.wav")
cat_sound = pygame.mixer.Sound("cat.wav")
pygame.mixer.music.load("theme.wav")

pygame.mixer.music.play(-1)
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
        self.muzzle = pygame.Rect(pygame.mouse.get_pos()[0]-(gun_dm["width"]/2)+23, pygame.mouse.get_pos()[1]-(gun_dm["height"]/2)+26, 30, 36)
        #self.hitbox = pygame.Rect(self.position.x, self.position.y, gun_dm["width"], gun_dm["height"])
    def update(self):
        self.position = Pair(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.muzzle = pygame.Rect(pygame.mouse.get_pos()[0]-(gun_dm["width"]/2)+23, pygame.mouse.get_pos()[1]-(gun_dm["height"]/2)+26, 30, 36)
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
            #pygame.draw.rect(screen, (255), gun.muzzle)
            # add sound
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
        self.position = Pair(random.randint(0,w-20), random.randint(0,h-20))
        self.velocity = Pair(random.randint(1,5), random.randint(1,5))
        self.dimensions = Pair(fly_dm["width"], fly_dm["height"])
        self.hitbox = pygame.Rect(self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
        self.alive = True
    def display(self):
        screen.blit(self.image, self.hitbox.topleft)
        #pygame.draw.rect(screen, (255,255,255), self.hitbox)
    def move(self):
        if self.alive == True:
            self.position += self.velocity
            self.hitbox.move_ip(self.velocity.x, self.velocity.y)
            if self.hitbox.right > w-20 or self.hitbox.left < 0:
                self.velocity.x = -self.velocity.x
            if self.hitbox.top < 0 or self.hitbox.bottom > h-20:
                self.velocity.y = - self.velocity.y
            self.ani_speed -= 1
            if self.ani_speed == 0:
                if self.ani_pos < 4:
                    self.image = self.sheet[self.ani_pos]
                    self.ani_pos += 1
                else:
                    self.ani_pos = 0
                self.ani_speed = 5
            screen.blit(self.image, self.hitbox.topleft)
    def die(self):
        self.alive = False
        self.image = self.dead
        self.velocity = Pair(0,0)
        pygame.mixer.Sound.play(hit_sound)
    def update(self):
        screen.blit(self.image, self.hitbox.topleft)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        screen.blit(self.image, self.rect)

class Cat:
    def __init__(self):
        self.sheet = [pygame.image.load("cat-1.png"), pygame.image.load("cat-2.png"), pygame.image.load("cat-3.png"), pygame.image.load("cat-4.png")]
        self.scared = pygame.image.load("cat-scared.png")
        self.ani_pos = 0
        self.image = self.sheet[self.ani_pos]
        self.ani_speed = 1
        self.position = Pair(100, 100)
        self.velocity = Pair(5, 0)
        self.dimensions = Pair(cat_dm["width"], cat_dm["height"])
        self.hitbox = pygame.Rect(self.position.x-(cat_dm["width"]/2)+35, self.position.y-(cat_dm["height"]/2)+30, 93, 55)
        self.alive = True
    def display(self):
        screen.blit(self.image, (self.position.x-(cat_dm["width"]/2), self.position.y-(cat_dm["height"]/2)))
        pygame.draw.rect(screen, (255,255,255), self.hitbox)
    def move(self):
        if self.alive == True:
            self.position += self.velocity
            self.hitbox.move_ip(self.velocity.x, self.velocity.y)
            self.ani_speed -= 1
            if self.ani_speed == 0:
                if self.ani_pos < 4:
                    self.image = self.sheet[self.ani_pos]
                    self.ani_pos += 1
                else:
                    self.ani_pos = 0
                self.ani_speed = 5
        #screen.blit(self.image, self.hitbox.topleft)
    def scare(self):
        self.alive = False
        #self.image = self.scared
        self.velocity = Pair(0,0)
        pygame.mixer.Sound.play(cat_sound)
    #def update(self):
        #screen.blit(self.image, self.hitbox.topleft)

def gameOver():
    global finished
    finished = True


flies = []
gun = Gun()
#cat = Cat()
score = 0
font = pygame.font.Font("rocksalt.ttf", 36)
start = 2000
finished = False
level = 2

def level1():
    global cat
    global level
    level = 1
    startlevel = 2000
    background = Background("marketplace.png", [0,0])
    #endbackground = Background("marketplace-blur.png", [0,0])
    cat = Cat()
    if not random.randrange(30):
        f = Fly()
        flies.append(f)

while True:
    screen.fill((0))
    clock.tick(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gun.display(x, y, "shoot")
            shot = True
            pygame.mixer.Sound.play(miss_sound)
            gun.ani_speed -= 1
            if gun.ani_speed == 0:
                shot = False
                gun.ani_speed == 10
                break
        else:
            shot = False
    while not finished:
        start -= 1
        if start <= 0:
            finished = True
        if level == 1:
            background = Background("marketplace.png", [0,0])
        elif level == 2:
            background = Background("outdoor.png", [0,0])
        x, y = pygame.mouse.get_pos()
        text = font.render("Score: "+str(score), True, (255,255,255))
        screen.blit(text, (30,30))
        level1()
        cat.display()
        cat.move()
        if gun.muzzle.colliderect(cat.hitbox) and shot:
        	finished = True
            #gameOver()
#       if not random.randrange(20):
#            f = Fly()
#            flies.append(f)
        for f in flies:
            f.display()
            f.move()
            if gun.muzzle.colliderect(f.hitbox) and shot:
                f.die()
                f.update()
                score += 1
        alive = []
        for f in flies:
            if f.alive == True:
                alive.append(f)
        flies = alive
        gun.display(x, y, "idle")
        gun.update()

        if finished:
            cat.scare()
            for f in flies:
                del f
            del cat
            del gun
            background = Background("marketplace-blur.png", [0,0])
            losemessage = font.render("Game over!", True, (255,255,255))
            fly_happy = pygame.image.load("fly-happy.png")
            screen.blit(fly_happy, (300,200))
            screen.blit(losemessage, (300,200))

        #if level cleared:
            #level += 1

        pygame.display.update()
