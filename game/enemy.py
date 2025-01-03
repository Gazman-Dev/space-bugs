import pygame
from pygame.math import Vector2
from typing import List
from game.bullet import Bullet
from configs.config import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.assets_loader import load_enemy_asset

class Enemy:
    def __init__(self, position: Vector2) -> None:
        self.position: Vector2 = position
        self.speed: float = ENEMY_SPEED
        self.direction: Vector2 = Vector2(0, 1)  # Moving downward by default
        self.bullets: List[Bullet] = []

        # Load and scale the image asset
        asset = load_enemy_asset()
        self.size: Vector2 = Vector2(asset.get_width(), asset.get_height())
        scale_factor = Vector2(SCREEN_WIDTH, SCREEN_HEIGHT) / self.size 
        self.image: pygame.Surface = pygame.transform.scale(asset, (int(self.size.x * scale_factor.x), int(self.size.y * scale_factor.y)))

    def move(self) -> None:
        self.position += self.direction * self.speed
        self.position.y = min(self.position.y, SCREEN_HEIGHT)  # Keeps the enemy inside screen bounds vertically

    def shoot(self) -> None:
        bullet_position = self.position + Vector2(0, self.size.y)
        bullet = Bullet(bullet_position)
        self.bullets.append(bullet)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.position)

    def check_collision(self, obj: pygame.Rect) -> bool:
        enemy_rect = self.image.get_rect(topleft=self.position)
        return enemy_rect.colliderect(obj)

    def update(self, screen: pygame.Surface) -> None:
        self.move()

        # Remove bullets that have gone beyond the screen boundaries
        self.bullets = [bullet for bullet in self.bullets if bullet.position.y < SCREEN_HEIGHT]

        for bullet in self.bullets:
            bullet.update()

        self.render(screen)

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
```
