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
pygame.display.set_caption("Flybusters")
clock = pygame.time.Clock()
h = screen.get_height()
w = screen.get_width()
mouse_x, mouse_y = pygame.mouse.get_pos()
miss_sound = pygame.mixer.Sound("miss.wav")
hit_sound = pygame.mixer.Sound("shotgun.wav")
cat_sound = pygame.mixer.Sound("cat.wav")
click_sound = pygame.mixer.Sound("click.wav")
pygame.mixer.music.load("theme.wav")
button_font = pygame.font.Font("gochi.ttf", 40)
big_font = pygame.font.Font("rocksalt.ttf", 40)
small_font = pygame.font.Font("gochi.ttf", 24)
pygame.mixer.music.play(-1)

class Button:
    def __init__(self, x, y, w, h, text):
        self.x= x
        self.y= y
        self.w= w
        self.h= h
        self.color = (255,255,255)
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.border = pygame.Rect(self.x-5, self.y-5, self.w+10, self.h+10)
    def display(self):
        text = button_font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (self.x + self.w/2, self.y + self.h/2)
        pygame.draw.rect(screen, (0,0,0), self.border)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(text, text_rect)
    def clicked(self):
        click = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        onButton = self.x < mouse_x < self.x + self.w and self.y < mouse_y < self.y + self.h
        if click[0] and onButton:
            pygame.mixer.Sound.play(click_sound)
            return True
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Pair(new_x, new_y)
class Gun:
    def __init__(self):
        self.sheet = [pygame.image.load("gun-1.png"),pygame.image.load("gun-2.png")]
        self.ani_pos = 0
        self.image = self.sheet[self.ani_pos]
        self.position = Pair(mouse_x, mouse_y)
        self.ani_speed = 10
        self.muzzle = pygame.Rect(pygame.mouse.get_pos()[0]-(gun_dm["width"]/2)+23, pygame.mouse.get_pos()[1]-(gun_dm["height"]/2)+26, 30, 36)
    def update(self):
        self.position = Pair(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.muzzle = pygame.Rect(pygame.mouse.get_pos()[0]-(gun_dm["width"]/2)+23, pygame.mouse.get_pos()[1]-(gun_dm["height"]/2)+26, 30, 36)
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
        self.position = Pair(random.randint(0,w-40), random.randint(0,h-40))
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
            if self.hitbox.right > w-40 or self.hitbox.left < 0:
                self.velocity.x = -self.velocity.x
            if self.hitbox.top < 0 or self.hitbox.bottom > h-40:
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
        self.position = Pair(100, random.randint(40, h-40))
        self.velocity = Pair(5, 0)
        self.dimensions = Pair(cat_dm["width"], cat_dm["height"])
        self.hitbox = pygame.Rect(self.position.x-(cat_dm["width"]/2)+35, self.position.y-(cat_dm["height"]/2)+30, 93, 55)
        self.alive = True
    def display(self):
        screen.blit(self.image, (self.position.x-(cat_dm["width"]/2), self.position.y-(cat_dm["height"]/2)))
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
    def scare(self):
        self.alive = False
        self.velocity = Pair(0,0)
        pygame.mixer.Sound.play(cat_sound)
    #def update(self):
        #screen.blit(self.image, self.hitbox.topleft)

flies = []
cats = []
gun = Gun()
score = 0
start = 0
finished = False
level = 2
home = True
info = False
p = 20
while True:
    screen.fill((0))
    clock.tick(200)
    start += 1
    print(start)
    if p > 8:
        if start%100 == 0:
            p -= 1
            print(p)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not finished and not home and not info:
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
    if home:
        background = Background("outdoor-blur.png", [0,0])
        play = Button(w/3 - 100, h/3, 200, 50, "Play")
        about = Button(2*(w/3) - 100, h/3, 200, 50, "About")
        play.display()
        about.display()
        if about.clicked():
            home = False
            info = True
        if play.clicked():
            home = False
    if info:
        background = Background("outdoor-blur.png", [0,0])
        photo = pygame.image.load("photo1.jpg")
        screen.blit(photo, (75,100))
        names = small_font.render("Yao and Oorja", True, (255,255,255))
        date = small_font.render("17 Dec 2017", True, (255,255,255))
        scribble = pygame.image.load("scribble.png")
        screen.blit(scribble, (400, 70))
        credits = ["Music: 'B00TE' on YouTube", "Effects: soundbible.com", "Fly sprite: Shauna Lynch", "Cat sprite: Agung Nugraha"]
        y = 140
        for i in credits:
            t = small_font.render(i, True, (255,255,255))
            screen.blit(t, (475,y))
            y += 40
        screen.blit(names, (75,300))
        screen.blit(date, (75,340))
        back = Button(w/2-100, 475, 200, 50, "Back")
        back.display()
        if back.clicked():
            home = True
            info = False
            finished = False
    if not finished and not home and not info:
        background = Background("d2-blur1.png", [0,0])
        x, y = pygame.mouse.get_pos()
        score_show = big_font.render("Score: "+str(score), True, (255,255,255))
        screen.blit(score_show, (30,30))
        if not random.randrange(60):
            cat = Cat()
            cats.append(cat)
        for c in cats:
            c.display()
            c.move()
            if gun.muzzle.colliderect(c.hitbox) and shot:
                c.scare()
                finished = True
        onscreen = []
        for c in cats:
            if c.alive == True and c.position.x <= w:
                onscreen.append(c)
        cats = onscreen
        if not random.randrange(p):
            f = Fly()
            flies.append(f)
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
    if finished and not home and not info:
        background = Background("d2-blur2.png", [0,0])
        losemessage = big_font.render("Game over!", True, (255,255,255))
        losemessage_rect = losemessage.get_rect()
        losemessage_rect.center = (w/2, h/2-30)
        score_rect = score_show.get_rect()
        score_rect.center = (w/2, h/2+25)
        fly_happy = pygame.image.load("fly-happy.png")
        scared_cat = pygame.image.load("cat-scared.png")
        screen.blit(fly_happy, (500,250))
        screen.blit(scared_cat, (-20,120))
        screen.blit(losemessage, losemessage_rect)
        screen.blit(score_show, score_rect)
        restart_button = Button(w/2-105, 50, 210, 60, "Play Again")
        restart_button.display()
        if restart_button.clicked():
            score = 0
            p = 20
            start = 0
            finished = False
        back = Button(w/2-50,130, 100, 40, "Home")
        back.display()
        if back.clicked():
            home = True
            info = False
    pygame.display.update()
