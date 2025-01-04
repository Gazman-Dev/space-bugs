import random
import pygame
from pygame.math import Vector2
from configs.config import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from game.utils.assets_loader import AssetsLoader

class Enemy:
    def __init__(self, position: Vector2) -> None:
        self.position: Vector2 = position
        self.speed: float = ENEMY_SPEED
        self.direction: Vector2 = Vector2(0, 1)  # Assuming the enemy moves downwards initially
        self.image: pygame.Surface = AssetsLoader.load_enemy_image()
        self.size: Vector2 = Vector2((SCREEN_WIDTH / 10), (SCREEN_HEIGHT / 10))
        self.image = pygame.transform.scale(self.image, (int(self.size.x), int(self.size.y)))
        self.rect: pygame.Rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.path: list[Vector2] = self.generate_random_path()
        self.current_target_index: int = 0
        self.sound_effects = self.load_sound_effects()  # Load sound effects
        Enemy.initialize_audio()
        Enemy.play_background_music()
        
    @staticmethod
    def initialize_audio() -> None:
        pygame.mixer.init()
        Enemy.background_music = pygame.mixer.Sound('assets/background_music.ogg')
        Enemy.sound_effects = {
            "move": pygame.mixer.Sound('assets/move_sound.ogg'),
            "collision": pygame.mixer.Sound('assets/collision_sound.ogg')
        }

    def load_sound_effects(self) -> dict:
        return {
            "move": pygame.mixer.Sound('assets/move_sound.ogg'),
            "collision": pygame.mixer.Sound('assets/collision_sound.ogg')
        }

    @staticmethod
    def play_background_music() -> None:
        Enemy.background_music.play(loops=-1)

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
                self.play_sound_effect("move")
            else:
                self.position += travel_vector

        self.rect.topleft = (self.position.x, self.position.y)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.position)

    def check_collision(self, obj: pygame.Rect) -> bool:
        collision = self.rect.colliderect(obj)
        if collision:
            self.play_sound_effect("collision")
        return collision

    def update(self) -> None:
        self.move()
        self.rect.topleft = (self.position.x, self.position.y)

    def render(self, screen: pygame.Surface) -> None:
        self.draw(screen)

    def play_sound_effect(self, effect_name: str) -> None:
        if effect_name in self.sound_effects:
            self.sound_effects[effect_name].play()