import pygame
from pygame.math import Vector2
from game.bullet import Bullet

import configs.config as config
import assets_loader as assets_loader


class Player:
    def __init__(self, start_position: Vector2):
        self.position: Vector2 = Vector2(start_position)
        self.speed: float = config.PLAYER_SPEED
        self.bullets: list = []
        self.direction: Vector2 = Vector2(0, 0)
        self.player_image: pygame.Surface = assets_loader.load('player_ship.png')

    def move(self, direction: Vector2) -> None:
        self.direction = direction

        # Update position using Vector2
        self.position += self.direction * self.speed

    def shoot(self) -> None:
        new_bullet = Bullet(self.position)
        self.bullets.append(new_bullet)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.player_image, self.position)

    def update(self) -> None:
        self.move(self.direction)
        for bullet in self.bullets:
            bullet.move()