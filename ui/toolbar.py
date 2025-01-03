import pygame
from configs.config import Config  # Assuming there's a Config file for general configurations

class Toolbar:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.score_position = pygame.Vector2(10, 10)  # Default position for displaying score
        self.health_position = pygame.Vector2(10, 40)  # Default position for displaying health

    def update(self, score: int, health: int):
        # This would typically update internal state if needed
        self.current_score = score
        self.current_health = health

    def draw(self):
        score_text = self.font.render(f"Score: {self.current_score}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.current_health}", True, (255, 255, 255))
        self.screen.blit(score_text, self.score_position)
        self.screen.blit(health_text, self.health_position)
```
