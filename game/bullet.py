import pygame
from pygame.math import Vector2

from game.utils.assets_loader import AssetsLoader


class Bullet:
    def __init__(self, position: Vector2, speed: float = 1, direction: Vector2 = Vector2(1, 0), radius: int = 5, color: tuple[int, int, int] = (255, 0, 0)):
        self.position = Vector2(position)
        self.speed = speed
        self.direction = Vector2(direction)
        self.radius = radius  # The visual size of the bullet on-screen.
        self.color = color    # The bullet's color, typically set to red.
        self.image = AssetsLoader.load_bullet_image()

    def move(self):
        self.position += self.speed * self.direction

    def update(self):
        self.move()

    def draw(self, surface: pygame.Surface):
        if self.image:
            surface.blit(self.image, (int(self.position.x), int(self.position.y)))
        else:
            pygame.draw.circle(surface, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def render(self, surface: pygame.Surface):
        self.draw(surface)

    def is_off_screen(self, screen_size: tuple[int, int]) -> bool:
        x, y = self.position
        width, height = screen_size
        return x < 0 or x > width or y < 0 or y > height