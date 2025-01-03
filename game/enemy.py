import pygame
from pygame.math import Vector2
import random

from configs.config import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from game.bullet import Bullet
<<<<<<< HEAD
from utils.assets_loader import load_enemy_asset
=======
from game.utils.assets_loader import AssetsLoader

>>>>>>> branch 'dev2' of https://github.com/IlyaGazman/space-bugs.git

class Enemy:
    def __init__(self, position: Vector2) -> None:
        self.position: Vector2 = position
        self.speed: float = ENEMY_SPEED
<<<<<<< HEAD
        self.direction: Vector2 = Vector2(0, 1)
        self.bullets: list[Bullet] = []
        self.image: pygame.Surface = load_enemy_asset()
=======
        self.direction: Vector2 = Vector2(0, 1)  # Assuming the enemy moves downwards initially
        self.image: pygame.Surface = AssetsLoader.load_enemy_image()
>>>>>>> branch 'dev2' of https://github.com/IlyaGazman/space-bugs.git
        self.size: Vector2 = Vector2((SCREEN_WIDTH / 10), (SCREEN_HEIGHT / 10))
        self.image = pygame.transform.scale(self.image, (int(self.size.x), int(self.size.y)))
        self.rect: pygame.Rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.path: list[Vector2] = self.generate_random_path()
        self.current_target_index: int = 0

    def generate_random_path(self) -> list[Vector2]:
        path = []
        max_coordinates = 8
        min_distance = 50
        for _ in range(max_coordinates):
            while True:
                new_point = Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
                if all(new_point.distance_to(point) >= min_distance for point in path):
                    path.append(new_point)
                    break
        return path

    def move(self) -> None:
        if self.path:
<<<<<<< HEAD
            target = self.path[self.current_target_index]
            vector_to_target = target - self.position
            if vector_to_target.length() != 0:
                self.direction = vector_to_target.normalize()
            
            travel_vector = self.direction * self.speed
            if vector_to_target.length() < travel_vector.length():
                self.position = target
                self.current_target_index = (self.current_target_index + 1) % len(self.path)
            else:
                self.position += travel_vector
=======
            target = self.path[self.current_target_index % len(self.path)]
            if self.position.distance_to(target) < self.speed:
                self.current_target_index = self.current_target_index + 1
                target = self.path[self.current_target_index % len(self.path)]
            self.direction = (target - self.position).normalize()
>>>>>>> branch 'dev2' of https://github.com/IlyaGazman/space-bugs.git
        
        self.rect.topleft = (self.position.x, self.position.y)

    def shoot(self) -> None:
        bullet_position = self.position + Vector2(0, 1)
        bullet = Bullet(bullet_position)
        self.bullets.append(bullet)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.position)
        for bullet in self.bullets:
            bullet.draw(surface)

    def check_collision(self, obj: pygame.Rect) -> bool:
        return self.rect.colliderect(obj)

    def update(self) -> None:
        self.move()
        self.rect.topleft = (self.position.x, self.position.y)
        self.position.x = max(0, min(self.position.x, SCREEN_WIDTH - self.size.x))
<<<<<<< HEAD
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT - self.size.y))
        self.bullets = [bullet for bullet in self.bullets if 0 <= bullet.position.y < SCREEN_HEIGHT]

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)

# Note: The Bullet class and its implementation should be defined elsewhere in the project.
=======
        self.position.y = max(0, min(self.position.y, SCREEN_HEIGHT - self.size.y))
>>>>>>> branch 'dev2' of https://github.com/IlyaGazman/space-bugs.git
