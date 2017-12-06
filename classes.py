class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Pair(new_x, new_y)
class Hand:
    def __init__(self):
        self.image = pygame.image.load("hand.png").convert_alpha()
        self.position = Pair(mouse[0], mouse[1])
        self.speed = 50
        self.hitbox = pygame.Rect(self.position.x, self.position.y, dm.hand_width, dm.hand_height)
    def display(self, x_pos, y_pos):
        screen.blit(self.image, (x_pos-(dm.hand_width/2), y_pos-(dm.hand_height/2)))
  #  def move(self):
