import pygame
from configs.config import PLAYER_SPEED, ENEMY_BULLET_SPEED

class Bullet:
    def __init__(self, position, speed, direction):
        self.position = position
        self.speed = speed
        self.direction = direction

    def move(self):
        self.position[0] += self.speed * self.direction[0]
        self.position[1] += self.speed * self.direction[1]

    def draw(self, surface):
        # Assume bullet is a circle for simplicity
        bullet_color = (255, 0, 0)  # Red color for the bullet
        bullet_radius = 5  # Example bullet radius
        pygame.draw.circle(surface, bullet_color, self.position, bullet_radius)
```
