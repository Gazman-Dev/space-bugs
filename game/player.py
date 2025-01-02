import pygame
import configs.config as config

class Player:
    def __init__(self, start_position):
        self.position = start_position
        self.speed = config.PLAYER_SPEED
        self.bullets = []

    def move(self, direction):
        if direction == "left":
            self.position[0] -= self.speed
        elif direction == "right":
            self.position[0] += self.speed
        elif direction == "up":
            self.position[1] -= self.speed
        elif direction == "down":
            self.position[1] += self.speed

    def shoot(self):
        new_bullet = Bullet(self.position)
        self.bullets.append(new_bullet)

    def draw(self, surface):
        # Assuming there is a function or a way to draw a player ship
        player_ship_image = pygame.image.load('images/player_ship.png')
        surface.blit(player_ship_image, self.position)

class Bullet:
    def __init__(self, start_position):
        self.position = list(start_position)  # Create a copy of start position
        self.speed = config.BULLET_SPEED

    def move(self):
        self.position[1] -= self.speed  # Move the bullet up the screen

    def draw(self, surface):
        bullet_image = pygame.image.load('images/bullet.png')
        surface.blit(bullet_image, self.position)

```
