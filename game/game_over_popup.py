import pygame


class GameOverPopup:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font(pygame.font.get_default_font(), 20)
        self.message = "Game over, the end"
        self.is_visible = False

    def show(self) -> None:
        self.is_visible = True

    def hide(self) -> None:
        self.is_visible = False

    def draw(self) -> None:
        if self.is_visible:
            message_surface = self.font.render(self.message, True, (255, 255, 255))
            instructions_surface = self.font.render("Press 'Esc' to exit or 'R' to reset.", True, (255, 255, 255))
            screen_rect = self.screen.get_rect()
            message_rect = message_surface.get_rect(center=(screen_rect.centerx, screen_rect.centery - 20))
            instructions_rect = instructions_surface.get_rect(center=(screen_rect.centerx, screen_rect.centery + 20))
            
            self.screen.blit(message_surface, message_rect)
            self.screen.blit(instructions_surface, instructions_rect)