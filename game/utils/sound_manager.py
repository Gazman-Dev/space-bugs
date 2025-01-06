import pygame
import os

class SoundManager:
    MOVE_SOUND: str = "sounds/move.wav"
    SHOOT_SOUND: str = "sounds/shoot.wav"
    BGM_SOUND: str = "sounds/bgm.mp3"
    EXPLOSION_SOUND: str = "sounds/explosion.wav"

    def __init__(self, sound_files: dict[str, str]):
        self.sound_files = sound_files
        self.loaded_sounds = {}

    def load_sounds(self) -> None:
        """Load sound files using pygame and store them in the loaded_sounds dictionary."""
        for name, path in self.sound_files.items():
            if os.path.exists(path):
                self.loaded_sounds[name] = pygame.mixer.Sound(path)

    def play_sound(self, sound_name: str, loop: bool = False) -> None:
        """Play a sound by name. Loop indefinitely if loop is True, else play once."""
        if sound_name in self.loaded_sounds:
            sound = self.loaded_sounds[sound_name]
            loops = -1 if loop else 0
            sound.play(loops=loops)

# Note: Before using SoundManager, ensure pygame mixer is initialized:
# pygame.mixer.init()

# Example usage:
# sound_files = {
#     "laser": "sounds/laser.wav",
#     "explosion": "sounds/explosion.wav",
# }
# manager = SoundManager(sound_files)
# manager.load_sounds()
# manager.play_sound("laser")