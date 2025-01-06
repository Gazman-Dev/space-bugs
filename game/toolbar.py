import pygame

from game.utils.sound_manager import SoundManager


class Toolbar:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font, sound_manager: SoundManager):
        self.screen = screen
        self.font = font
        self.score_position = pygame.Vector2(10, 10)  # Default position for displaying score
        self.health_position = pygame.Vector2(10, 40)  # Default position for displaying health
        self.current_score = -1
        self.current_health = -1
        self.sound_manager = sound_manager

    def update(self, score: int, health: int):
        # Adjust the display values for score and health on the toolbar
        self.current_score = score
        self.current_health = health

    def draw(self):
        score_text = self.font.render(f"Score: {self.current_score}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.current_health}", True, (255, 255, 255))
        self.screen.blit(score_text, self.score_position)
        self.screen.blit(health_text, self.health_position)