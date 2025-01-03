import pygame
from pygame.math import Vector2
from game.bullet import Bullet
from configs.config import ENEMY_SPEED

class Enemy:
    def __init__(self, position: Vector2):
        self.position: Vector2 = position
        self.speed: float = ENEMY_SPEED
        self.direction: Vector2 = Vector2(0, 1)  # Assuming the enemy moves downwards initially
        self.bullets: list[Bullet] = []

    def move(self) -> None:
        self.position += self.direction * self.speed

    def shoot(self) -> None:
        bullet_position = self.position + Vector2(0, 1)  # Example: starting just below the enemy
        bullet = Bullet(bullet_position)  # Assuming a Bullet class is defined elsewhere
        self.bullets.append(bullet)

    def draw(self, surface: pygame.Surface) -> None:
        enemy_image = pygame.Surface((50, 50))  # Placeholder for enemy image, 50x50 for example
        enemy_image.fill((255, 0, 0))  # Fill with red for visibility
        surface.blit(enemy_image, self.position)

    def check_collision(self, obj: pygame.Rect) -> bool:
        enemy_rect = pygame.Rect(self.position.x, self.position.y, 50, 50)  # Assuming the enemy is 50x50
        if enemy_rect.colliderect(obj):
            return True
        return False

    def update(self) -> None:
        self.move()
        # Check for bullet collisions or other updates needed for each enemy

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)  # Assuming Bullet class has a draw method

# Note: The Bullet class and its implementation should be defined elsewhere in the project.