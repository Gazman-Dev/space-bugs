import pygame

from game.game import Game
from game.utils.sound_manager import SoundManager


def main() -> None:
    # Initialize pygame
    pygame.init()
    
    # Create a SoundManager instance
    sound_manager = SoundManager()
    # Preload all necessary sound effects for the game
    sound_manager.load_sounds()
    
    # Create a Game instance
    game_instance = Game(sound_manager)

    # Call the setup function of Game instance
    game_instance.setup()

    # Main game loop
    running = True
    while running:
        # Execute game_loop() from Game instance
        running = game_instance.game_loop()
        
        # Interspersed sound controls
        # Example of sound event calls (Assuming these are implemented appropriately in the game's architecture)
        # sound_manager.play_sound(SoundManager.MOVE_SOUND)
        # sound_manager.play_sound(SoundManager.SHOOT_SOUND)
        # sound_manager.play_sound(SoundManager.BGM_SOUND)
        # sound_manager.play_sound(SoundManager.EXPLOSION_SOUND)

if __name__ == "__main__":
    main()