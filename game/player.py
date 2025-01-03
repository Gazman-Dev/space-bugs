import pygame
import configs.config as config
from pygame.math import Vector2
import assets_loader

class Player:
    def __init__(self):
        self.position: Vector2 = Vector2(config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)
        self.speed: float = config.PLAYER_SPEED
        self.bullets: list = []
        self.direction: Vector2 = Vector2(0, 0)
        self.player_image: pygame.Surface = assets_loader.load_player_image()
        self.size: Vector2 = Vector2(config.PLAYER_SIZE[0], config.PLAYER_SIZE[1])

    def move(self, direction: Vector2) -> None:
        self.direction = direction
        new_position = self.position + (self.direction * self.speed)
        if 0 <= new_position.x <= config.SCREEN_WIDTH - self.size.x and 0 <= new_position.y <= config.SCREEN_HEIGHT - self.size.y:
            self.position = new_position

    def shoot(self) -> None:
        bullet_position = Vector2(self.position.x + self.size.x / 2, self.position.y)
        new_bullet = Bullet(position=bullet_position)
        self.bullets.append(new_bullet)

    def draw(self, surface: pygame.Surface) -> None:
        scaled_image = pygame.transform.scale(self.player_image, (int(self.size.x), int(self.size.y)))
        surface.blit(scaled_image, (self.position.x, self.position.y))

    def update(self, screen: pygame.Surface) -> None:
        keys = pygame.key.get_pressed()
        self.move(Vector2((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]), (keys[pygame.K_DOWN] - keys[pygame.K_UP])))
        
        if keys[pygame.K_SPACE]:
            self.shoot()

        for bullet in self.bullets:
            bullet.update()

        self.draw(screen)

class Bullet:
    def __init__(self, position: Vector2):
        self.position: Vector2 = position
        self.speed: float = config.BULLET_SPEED
        self.bullet_image: pygame.Surface = assets_loader.load_bullet_image()

    def update(self) -> None:
        self.position.y -= self.speed

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.bullet_image, (self.position.x, self.position.y))
```

Please note that you need to have appropriate definitions for `assets_loader.load_player_image()`, `assets_loader.load_bullet_image()`, and `config` module which should contain attributes like `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `PLAYER_SPEED`, `PLAYER_SIZE`, `BULLET_SPEED`, etc.
