import pygame
from configs.config import ENEMY_SPEED

class Enemy:
    def __init__(self, position):
        self.position = position
        self.speed = ENEMY_SPEED
        self.direction = pygame.Vector2(0, 1)  # Assuming the enemy moves downwards initially
        self.bullets = []

    def move(self):
        self.position += self.direction * self.speed

    def shoot(self):
        bullet_position = self.position + pygame.Vector2(0, 1)  # Example: starting just below the enemy
        bullet = Bullet(bullet_position)  # Assuming a Bullet class is defined elsewhere
        self.bullets.append(bullet)

    def draw(self, surface):
        enemy_image = pygame.Surface((50, 50))  # Placeholder for enemy image, 50x50 for example
        enemy_image.fill((255, 0, 0))  # Fill with red for visibility
        surface.blit(enemy_image, self.position)

    def check_collision(self, obj):
        enemy_rect = pygame.Rect(self.position.x, self.position.y, 50, 50)  # Assuming the enemy is 50x50
        if enemy_rect.colliderect(obj):
            return True
        return False

# Note: The Bullet class and its implementation should be defined elsewhere in the project.
```

Note:
- This code assumes you have a configuration file with an `ENEMY_SPEED` variable defined.
- The `Bullet` class is assumed to be defined elsewhere in the project, so its instantiation may need adjustments based on its actual implementation.
- The `enemy_image` is simply a placeholder surface here and should ideally be replaced with an actual enemy sprite loaded from assets.
