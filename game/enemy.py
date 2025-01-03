import pygame
from pygame.math import Vector2

from configs.config import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from game.bullet import Bullet
from utils.assets_loader import load_enemy_asset

class Enemy:
    def __init__(self, position: Vector2) -> None:
        self.position: Vector2 = position
        self.speed: float = ENEMY_SPEED
        self.direction: Vector2 = Vector2(0, 1)  # Assuming the enemy moves downwards initially
        self.bullets: list[Bullet] = []
        self.image: pygame.Surface = load_enemy_asset()
        self.size: Vector2 = Vector2((SCREEN_WIDTH / 10), (SCREEN_HEIGHT / 10))
        self.image = pygame.transform.scale(self.image, (int(self.size.x), int(self.size.y)))
        self.rect: pygame.Rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def move(self) -> None:
        self.position += self.direction * self.speed
        self.rect.topleft = (self.position.x, self.position.y)

    def shoot(self) -> None:
        bullet_position = self.position + Vector2(0, 1)  # Example: starting just below the enemy
        bullet = Bullet(bullet_position)  # Assuming a Bullet class is defined elsewhere
        self.bullets.append(bullet)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.position)  # Use the loaded image for rendering

    def check_collision(self, obj: pygame.Rect) -> bool:
        if self.rect.colliderect(obj):
            return True
        return False

    def update(self) -> None:
        self.move()
        # Update rect alignment if necessary
        self.rect.topleft = (self.position.x, self.position.y)
        self.position.x = max(0, min(self.position.x, SCREEN_WIDTH - self.size.x))
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT - self.size.y))
        # Filter out bullets that are off screen
        self.bullets = [bullet for bullet in self.bullets if 0 <= bullet.position.y < SCREEN_HEIGHT]

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)  # Assuming Bullet class has a draw method

# Note: The Bullet class and its implementation should be defined elsewhere in the project.