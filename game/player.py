import pygame
import configs.config as config
from pygame.math import Vector2
import assets.images as images  # Updated import

class Player:
    def __init__(self, start_position):
        self.position = Vector2(start_position)
        self.speed = config.PLAYER_SPEED
        self.bullets = []
        self.direction = Vector2(0, 0)  # Added direction attribute

    def move(self, direction):
        if direction == "left":
            self.direction = Vector2(-1, 0)
        elif direction == "right":
            self.direction = Vector2(1, 0)
        elif direction == "up":
            self.direction = Vector2(0, -1)
        elif direction == "down":
            self.direction = Vector2(0, 1)
        else:
            self.direction = Vector2(0, 0)
        
        # Update position using Vector2
        self.position += self.direction * self.speed

    def shoot(self):
        new_bullet = Bullet(self.position)
        self.bullets.append(new_bullet)

    def draw(self, surface):
        # Updated to use 'images' import if required
        player_ship_image = pygame.image.load('images/player_ship.png')
        surface.blit(player_ship_image, self.position)

    def update(self):
        self.move(self.direction)  # Integrate movement update
        for bullet in self.bullets:
            bullet.move()

class Bullet:
    def __init__(self, start_position):
        self.position = Vector2(start_position)  # Use Vector2 for position
        self.speed = config.BULLET_SPEED

    def move(self):
        self.position.y -= self.speed  # Move the bullet up the screen

    def draw(self, surface):
        bullet_image = pygame.image.load('images/bullet.png')
        surface.blit(bullet_image, self.position)