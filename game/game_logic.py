import pygame
import random
import time
from pygame.math import Vector2

from configs.config import MAX_ENEMIES, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.bullet import Bullet
from game.enemy import Enemy
from game.player import Player


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

    def setup(self) -> None:
        self.player = Player()
        # Initialize enemies here based on game level
        self.spawn_enemies()

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

    def check_collisions(self) -> None:
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect().colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    # Handle what happens when an enemy is hit, e.g., increase score

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
        pygame.display.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(Vector2(self.player.rect.centerx, self.player.rect.top))
                    self.bullets.append(bullet)


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.game_loop()
    pygame.quit()