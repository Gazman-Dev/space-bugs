import pygame
import random
import time
from pygame.math import Vector2

from configs.config import MAX_ENEMIES, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.bullet import Bullet
from game.enemy import Enemy
from game.player import Player
from game.toolbar import Toolbar  # Added import for Toolbar


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.player: Player = None
        self.enemies: list[Enemy] = []
        self.bullets: list[Bullet] = []
        self.running: bool = True
        self.last_enemy_spawn_time: float = time.time()
        self.toolbar: Toolbar = Toolbar()  # Initialize toolbar

    def setup(self) -> None:
        self.player = Player()
        # Initialize enemies here based on game level
        self.spawn_enemies()
        # Initialize toolbar for game stats display
        self.toolbar.setup()

    def spawn_enemies(self) -> None:
        current_time = time.time()
        if len(self.enemies) < MAX_ENEMIES and (current_time - self.last_enemy_spawn_time) > 2:
            enemy = Enemy(Vector2(random.randint(0, SCREEN_WIDTH - 50), 50))
            self.enemies.append(enemy)
            self.last_enemy_spawn_time = current_time

    def game_loop(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(FPS)
            self.spawn_enemies()
            self.toolbar.update(self.player.health, self.player.score)  # Update toolbar with live stats

    def check_collisions(self) -> None:
        bullets_to_remove = []
        enemies_to_remove = []

        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect().colliderect(enemy.rect):
                    enemies_to_remove.append(enemy)
                    bullets_to_remove.append(bullet)
                    # Increase score on hitting an enemy
                    self.player.score += enemy.value

        # Remove bullets and enemies after iteration to avoid modifying the list during iteration
        for bullet in bullets_to_remove:
            if bullet in self.bullets:
                self.bullets.remove(bullet)

        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)

        # Check player health/game over condition
        if self.player.health <= 0:
            self.running = False
            print("Game Over!")  # Placeholder for game over sequence

    def update(self) -> None:
        self.player.update(self.screen)
        for enemy in self.enemies:
            enemy.update()
        for bullet in self.bullets:
            bullet.update(self.screen)
            if bullet.rect().bottom < 0:
                self.bullets.remove(bullet)

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        self.toolbar.draw(self.screen)  # Draw toolbar with current game stats
        pygame.display.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(Vector2(self.player.rect.centerx, self.player.rect.top))
                    self.bullets.append(bullet)
                # Example additional key action
                elif event.key == pygame.K_r:
                    self.__init__()  # Restart game by reinitializing
                    self.setup()


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.game_loop()
    pygame.quit()