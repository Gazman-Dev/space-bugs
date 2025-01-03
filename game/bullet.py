import pygame
from pygame.math import Vector2

from game.utils.assets_loader import AssetsLoader


class Bullet:
    def __init__(self, position: Vector2, speed: float = 1, direction: Vector2 = Vector2(1, 0), radius: int = 5, color: tuple[int, int, int] = (255, 0, 0)):
        self.position = Vector2(position)  # starting coordinates for the bullet.
        self.speed = speed                 # bullet speed value.
        self.direction = Vector2(direction)# direction vector for bullet movement.
        self.radius = radius               # bullet's visual size on the screen.
        self.color = color                 # RGB color value of the bullet.

    def move(self):
        # Updates position by applying speed and direction, adjusted for elapsed time
        self.position += self.speed * self.direction

    def update(self, surface: pygame.Surface):
        self.move()
        # Assuming additional code to ensure position stays within provided surface boundaries would be here

    def draw(self, surface: pygame.Surface):
        # Adjusts bullet position based on screen dimensions and draws it using specified radius and color
        pygame.draw.circle(surface, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def render(self, surface: pygame.Surface):
        self.draw(surface)

    def is_off_screen(self, screen_size: tuple[int, int]) -> bool:
        x, y = self.position
        width, height = screen_size
        return x < 0 or x > width or y < 0 or y > height

    def rect(self) -> pygame.Rect:
        # Provides Rect object of bullet's position
        return pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)