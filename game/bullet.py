import pygame
from pygame.math import Vector2

class Bullet:
    def __init__(self, position, speed, direction):
        self.position = Vector2(position)
        self.speed = speed
        self.direction = Vector2(direction)

    def move(self):
        self.position += self.speed * self.direction

    def draw(self, surface):
        # Assume bullet is a circle for simplicity
        bullet_color = (255, 0, 0)  # Red color for the bullet
        bullet_radius = 5  # Example bullet radius
        pygame.draw.circle(surface, bullet_color, (int(self.position.x), int(self.position.y)), bullet_radius)