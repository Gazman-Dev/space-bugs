import pygame
from pygame.math import Vector2
from game.utils.sound_manager import SoundManager


class Bullet:
    def __init__(self, position: Vector2, speed: float, direction: Vector2, 
                 radius: int = 5, color: tuple[int, int, int] = (255, 0, 0), sound_manager: SoundManager = None):
        self.position = Vector2(position)  # starting coordinates for the bullet.
        self.speed = speed  # bullet speed value.
        self.direction = Vector2(direction)  # direction vector for bullet movement.
        self.radius = radius  # bullet's visual size on the screen.
        self.color = color  # RGB color value of the bullet.
        self.sound_manager = sound_manager  # instance to manage bullet-related sound effects.

    def move(self):
        # Updates position by applying speed and direction, adjusted for elapsed time
        self.position += self.speed * self.direction

    def update(self, surface: pygame.Surface):
        self.move()
        # Assuming additional code to ensure position stays within provided surface boundaries would be here

    def draw(self, surface: pygame.Surface):
        # Adjusts bullet position based on screen dimensions and draws it using specified radius and color
        pygame.draw.circle(surface, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def play_shooting_sound(self):
        if self.sound_manager:
            self.sound_manager.play()  # Uses sound_manager to play the shooting sound

    def is_off_screen(self, screen_size: tuple[int, int]) -> bool:
        x, y = self.position
        width, height = screen_size
        off_screen = x < 0 or x > width or y < 0 or y > height
        if off_screen and self.sound_manager:
            self.sound_manager.play()  # Uses sound_manager to play an out-of-bound sound
        return off_screen

    def rect(self) -> pygame.Rect:
        # Provides Rect object of bullet's position
        return pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2)