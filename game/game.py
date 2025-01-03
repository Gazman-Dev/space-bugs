import pygame
from game.snake import Snake
from game.food import Food
from game.toolbar import Toolbar
import configs.config as config

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Space Bugs")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 48)
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.health = 100
        self.running = True
        self.toolbar = None

    def setup(self):
        self.toolbar = Toolbar(self.screen)
        self.toolbar.update(self.score, self.health)
        self.register_events()

    def register_events(self):
        pygame.key.set_repeat(1, 50)

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.snake.update()
            self.food.update()

            if self.snake.check_collision_with_wall() or self.snake.check_collision_with_self():
                self.show_game_over()
                self.running = False
                return

            if self.snake.check_collision_with_food(self.food):
                self.score += 10
                self.health += 5
                self.food.reposition()

            self.toolbar.update(self.score, self.health)
            self.render()
            self.clock.tick(config.FPS)

    def render(self):
        self.screen.fill(config.BG_COLOR)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.toolbar.draw()
        pygame.display.flip()

    def show_game_over(self):
        game_over_surface = self.font.render('Game Over', True, config.TEXT_COLOR)
        self.screen.blit(game_over_surface, (config.SCREEN_WIDTH // 2 - game_over_surface.get_width() // 2, config.SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.game_loop()
    pygame.quit()
```
