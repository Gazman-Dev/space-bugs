import pygame

import configs.config
from game.bullet import Bullet
from game.enemy import Enemy
from game.player import Player
from pygame.math import Vector2  # Ensure that Vector2 is imported

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((configs.config.SCREEN_WIDTH, configs.config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = None
        self.enemies = []
        self.bullets = []
        self.running = True

    def setup(self):
        self.player = Player(Vector2(self.screen.get_width() // 2, self.screen.get_height() - 50))
        # Initialize enemies here based on game level
        for i in range(5):  # Example of creating 5 enemies
            enemy = Enemy(Vector2(100 * i, 50))
            self.enemies.append(enemy)

    def game_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.check_collisions()
            self.render()
            self.clock.tick(configs.config.FPS)

    def check_collisions(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    # Handle what happens when an enemy is hit, e.g., increase score

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Add bullet firing logic
                    bullet = Bullet(Vector2(self.player.rect.centerx, self.player.rect.top))
                    self.bullets.append(bullet)


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.game_loop()
    pygame.quit()