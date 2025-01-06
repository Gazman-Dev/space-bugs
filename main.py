import pygame
from game.game_logic import Game
from sound.sound_manager import SoundManager

def main() -> None:
    # Initialize pygame
    pygame.init()
    
    # Create a SoundManager instance
    sound_manager = SoundManager()
    # Preload all necessary sound effects for the game
    sound_manager.load_sounds()
    
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