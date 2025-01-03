import pygame
from pygame.math import Vector2


class Bullet:
    def __init__(self, position, speed, direction, radius=5, color=(255, 0, 0)):
        self.position = Vector2(position)
        self.speed = speed
        self.direction = Vector2(direction)
        self.radius = radius  # The visual size of the bullet on-screen.
        self.color = color    # The bullet's color, typically set to red.

    def move(self):
        self.position += self.speed * self.direction

    def update(self):
        self.move()

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def render(self, surface):
        self.draw(surface)

    def is_off_screen(self, screen_size):
        x, y = self.position
        width, height = screen_size
        return x < 0 or x > width or y < 0 or y > height