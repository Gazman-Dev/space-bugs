import pygame
from game.game_logic import Game

def main():
    # Initialize pygame
    pygame.init()
    
    # Create a Game instance
    game_instance = Game()

    # Call the setup function of Game instance
    game_instance.setup()

    # Main game loop
    running = True
    while running:
        # Execute game_loop() from Game instance
        running = game_instance.game_loop()

if __name__ == "__main__":
    main()

