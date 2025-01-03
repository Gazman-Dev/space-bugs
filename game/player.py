import pygame
from pygame.math import Vector2

import configs.config as config
from game.bullet import Bullet
from game.utils.assets_loader import AssetsLoader


class Player:
    def __init__(self, start_position: Vector2):
        self.position: Vector2 = Vector2(start_position)
        self.speed: float = config.PLAYER_SPEED
        self.bullets: list = []
        self.direction: Vector2 = Vector2(0, 0)
        self.player_image: pygame.Surface = AssetsLoader.load_player_image()
        self.size: Vector2 = Vector2(self.player_image.get_width(), self.player_image.get_height())

    def move(self, direction: Vector2) -> None:
        self.direction = direction

        # Update position using Vector2
        self.position += self.direction * self.speed

        # Ensure player stays within screen bounds using config values
        screen_size = [config.SCREEN_WIDTH, config.SCREEN_HEIGHT]
        self.position.x = max(0, min(self.position.x, screen_size[0] - self.size.x))
        self.position.y = max(0, min(self.position.y, screen_size[1] - self.size.y))

    def shoot(self) -> None:
        new_bullet = Bullet(self.position)
        self.bullets.append(new_bullet)

    def draw(self, surface: pygame.Surface) -> None:
        # Render player ship image on surface
        surface.blit(self.player_image, self.position)

    def update(self, screen: pygame.Surface) -> None:
        self.move(self.direction)
        for bullet in self.bullets:
            bullet.move()

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)
        # Additional rendering logic can be added here, e.g., bullets, enemies