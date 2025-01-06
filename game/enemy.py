import random

import pygame
from pygame.math import Vector2

from configs.config import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from game.utils.assets_loader import AssetsLoader
from game.utils.sound_manager import SoundManager


class Enemy:
    def __init__(self, position: Vector2, sound_manager: SoundManager) -> None:
        self.position: Vector2 = position
        self.speed: float = ENEMY_SPEED
        self.direction: Vector2 = Vector2(0, 1)  # Assuming the enemy moves downwards initially
        self.image: pygame.Surface = AssetsLoader.load_enemy_image()
        self.size: Vector2 = Vector2((SCREEN_WIDTH / 10), (SCREEN_HEIGHT / 10))
        self.image = pygame.transform.scale(self.image, (int(self.size.x), int(self.size.y)))
        self.rect: pygame.Rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.path: list[Vector2] = self.generate_random_path()
        self.current_target_index: int = 0
        self.sound_manager: SoundManager = sound_manager

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

        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.position)

    def update(self) -> None:
        self.move()
        self.rect.topleft = (self.position.x, self.position.y)

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)