import pygame
from music_player import MusicPlayer
from game.snake import Snake
from game.food import Food
from configs.config import Config
from pygame.math import Vector2

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True
        self.music_player = MusicPlayer()

    def setup(self):
        # Initialize score toolbar
        # Update this method according to your toolbar specifics
        self.food.update_position()
        self.register_events()
        self.music_player.load_track('path/to/music/file')
        self.music_player.play(loop=True)

    def register_events(self):
        # Example of registering event, modify as needed
        pygame.key.set_repeat(100, 50)
        # other event registration or key bindings

    def game_loop(self):
        while self.running:
            self.snake.grow()
            if self.snake.collides_with_wall() or self.snake.collides_with_self():
                self.music_player.stop()
                self.show_game_over()
                self.running = False
                return
            elif not self.snake.collides_with_food(self.food):
                self.snake.trim_tail()
            self.update_food_position()
            self.render()
            self.clock.tick(Config.FPS)

    def update_food_position(self):
        self.food.update_position()
        if self.food.collides_with_snake(self.snake):
            self.food.update_position()

    def render(self):
        self.screen.fill((0, 0, 0))  # clear screen with black
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self.manage_music_transitions()
        pygame.display.flip()

    def manage_music_transitions(self):
        # Implement logic for music scene transitions if needed
        pass

    def show_game_over(self):
        # Display "Game Over" text
        text = self.font.render('Game Over', True, (255, 0, 0))
        self.screen.blit(text, (Config.SCREEN_WIDTH // 2 - text.get_width() // 2, Config.SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # wait for 2 seconds before closing
        self.music_player.handle_game_over_transition()

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.game_loop()
```
