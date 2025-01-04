import pygame


class Toolbar:
    def __init__(self):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.score_position = pygame.Vector2(10, 10)  # Default position for displaying score
        self.health_position = pygame.Vector2(10, 40)  # Default position for displaying health
        self.current_score = -1
        self.current_health = -1

    def update(self, score: int, health: int):
        # This would typically update internal state if needed
        self.current_score = score
        self.current_health = health

    def draw(self, surface: pygame.Surface):
        score_text = self.font.render(f"Score: {self.current_score}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.current_health}", True, (255, 255, 255))
        surface.blit(score_text, self.score_position)
        surface.blit(health_text, self.health_position)
