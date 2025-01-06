import pygame
import path.to.sound_manager  # for accessing SoundManager class

class Toolbar:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.score_position = pygame.Vector2(10, 10)  # Default position for displaying score
        self.health_position = pygame.Vector2(10, 40)  # Default position for displaying health
        self.current_score = -1
        self.current_health = -1
        self.sound_manager = path.to.sound_manager.SoundManager()  # Creates instance of SoundManager

    def update(self, score: int, health: int):
        # Adjust the display values for score and health on the toolbar
        self.current_score = score
        self.current_health = health

    def draw(self):
        score_text = self.font.render(f"Score: {self.current_score}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.current_health}", True, (255, 255, 255))
        self.screen.blit(score_text, self.score_position)
        self.screen.blit(health_text, self.health_position)

        # Example of utilizing the SoundManager (with hypothetical constants)
        # self.sound_manager.play(path.to.sound_manager.MOVE_SOUND)
        # self.sound_manager.play(path.to.sound_manager.SHOOT_SOUND)
        # Apply other sound effects as needed like:
        # self.sound_manager.play(path.to.sound_manager.BGM_SOUND)
        # self.sound_manager.play(path.to.sound_manager.EXPLOSION_SOUND)