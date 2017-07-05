import pygame
from image_loader import *

class Mob(pygame.sprite.Sprite):
    def __init__(self, image, x, y, hp):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = hp
        self.damage = 20

    def follow_hero(self, Hero):
        #find direction vector from hero to enemy
        direction_x = self.rect.x - Hero.rect.x
        direction_y = self.rect.y - Hero.rect.y
        direction = math.hypot(direction_x, direction_y)
        direction_x /= direction
        direction_y /= direction
        self.rect.x += self.speed * direction_x
        self.rect.y += self.speed * direction_y

    def movement(self, x, y):
        self.rect.move_ip(x,y)

class ShrimpMob(Mob):
    def __init__(self, x, y):
        self.walk1 = pygame.image.load('images/mobs/shrimp/left/walk1.png')
        Mob.__init__(self, self.walk1, x, y, 100)

        self.walk2 = pygame.image.load('images/mobs/shrimp/left/walk2.png')

        self.aggro1 = pygame.image.load('images/mobs/shrimp/left/aggro1.png')
        self.aggro2 = pygame.image.load('images/mobs/shrimp/left/aggro2.png')

        self.neutral_animation = [self.walk1, self.walk2]
        self.aggro_animation = [self.aggro1, self.aggro2]

        self.speed = 5

        self.current_frame = 0
        self.ticker = 0

    def update(self):
        self.image = self.neutral_animation[self.current_frame]

        self.ticker += 1
        if self.ticker % 15 == 0:
            self.current_frame = (self.current_frame + 1) % 2
            self.ticker = 0