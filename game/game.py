import random
import time

import pygame
from pygame.math import Vector2

from configs.config import MAX_ENEMIES, SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game.bullet import Bullet
from game.enemy import Enemy
from game.game_over_popup import GameOverPopup
from game.player import Player
from game.toolbar import Toolbar
from game.utils.sound_manager import SoundManager


class Game:
    def __init__(self, sound_manager: SoundManager) -> None:
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.player: Player | None = None
        self.enemies: list[Enemy] = []
        self.bullets: list[Bullet] = []
        self.running: bool = True
        self.last_enemy_spawn_time: float = time.time()
        self.toolbar: Toolbar = Toolbar(screen=self.screen, sound_manager=sound_manager)
        self.player_health: int = 5
        self.score: int = 0
        self.shake_intensity: int = 0
        self.sound_manager: SoundManager = sound_manager
        self.game_over_popup: GameOverPopup = GameOverPopup(self.screen)

    def setup(self) -> None:
        self.player = Player(self.sound_manager)
        self.spawn_enemies()
        self.player_health = 5
        self.score = 0
        self.shake_intensity = 0
        self.sound_manager.play_sound(SoundManager.BGM_SOUND)

    def spawn_enemies(self) -> None:
        current_time = time.time()
        if len(self.enemies) < MAX_ENEMIES and (current_time - self.last_enemy_spawn_time) > 2:
            enemy = Enemy(Vector2(random.randint(0, SCREEN_WIDTH - 50), 50), self.sound_manager)
            self.enemies.append(enemy)
            self.last_enemy_spawn_time = current_time

    def game_loop(self) -> None:
        while self.running:
            self.handle_events()
            if not self.game_over_popup.is_visible:
                self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(FPS)
            self.spawn_enemies()
            self.toolbar.update(self.score, self.player_health)
            if not self.running and self.player_health <= 0:
                self.display_game_over_popup()

    def check_collisions(self) -> None:
        self.check_bullet_collisions()
        self.check_player_collisions()

    def check_bullet_collisions(self) -> None:
        bullets_to_remove = []
        enemies_to_remove = []

        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect().colliderect(enemy.rect):
                    enemies_to_remove.append(enemy)
                    bullets_to_remove.append(bullet)
                    self.score += 1
                    self.sound_manager.play_sound(SoundManager.EXPLOSION_SOUND)

        for bullet in bullets_to_remove:
            if bullet in self.bullets:
                self.bullets.remove(bullet)

        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)

    def check_player_collisions(self) -> None:
        enemies_to_remove = []

        for enemy in self.enemies:
            if self.player and enemy.rect.colliderect(self.player.rect):
                enemies_to_remove.append(enemy)
                self.player_health -= 1
                self.apply_screen_shake()
                self.sound_manager.play_sound(SoundManager.GAME_OVER)
                if self.player_health <= 0:
                    self.display_game_over_popup()

        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)

    def update(self) -> None:
        if self.player:
            self.player.update(self.screen)
        for enemy in self.enemies:
            enemy.update()
        for bullet in self.bullets:
            bullet.update(self.screen)
            if bullet.rect().bottom < 0:
                self.bullets.remove(bullet)

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        if self.player:
            self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        self.toolbar.draw()
        self.game_over_popup.draw()
        pygame.display.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.K_r:
                self.reset_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player:
                    bullet = Bullet(Vector2(self.player.rect.centerx, self.player.rect.top),
                                    sound_manager=self.sound_manager)
                    self.bullets.append(bullet)
                    self.sound_manager.play_sound(SoundManager.SHOOT_SOUND)
                elif event.key == pygame.K_r:
                    self.__init__(self.sound_manager)
                    self.setup()

    def apply_screen_shake(self) -> None:
        pass

    def display_game_over_popup(self) -> None:
        self.game_over_popup.is_visible = True

    def reset_game(self):
        self.game_over_popup.is_visible = False
        self.player_health = 5
        self.score = 0
