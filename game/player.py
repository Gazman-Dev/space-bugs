import pygame
import configs.config as config
from pygame.math import Vector2

class Player:
    def __init__(self, start_position):
        self.position = Vector2(start_position)
        self.speed = config.PLAYER_SPEED
        self.bullets = []

    def move(self, direction):
        if direction == "left":
            self.position.x -= self.speed
        elif direction == "right":
            self.position.x += self.speed
        elif direction == "up":
            self.position.y -= self.speed
        elif direction == "down":
            self.position.y += self.speed

    def shoot(self):
        new_bullet = Bullet(self.position)
        self.bullets.append(new_bullet)

    def draw(self, surface):
        # Assuming there is a function or a way to draw a player ship
        player_ship_image = pygame.image.load('images/player_ship.png')
        surface.blit(player_ship_image, self.position)

class Bullet:
    def __init__(self, start_position):
        self.position = Vector2(start_position)  # Use Vector2 for position
        self.speed = config.BULLET_SPEED

    def move(self):
        self.position.y -= self.speed  # Move the bullet up the screen

    def draw(self, surface):
        bullet_image = pygame.image.load('images/bullet.png')
        surface.blit(bullet_image, self.position)