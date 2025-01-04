import pygame
import os

class SoundManager:
    def __init__(self, sound_directory: str):
        self.sound_directory = sound_directory
        self.loaded_sounds = {}

    def load_sound_effects(self, sound_files: list):
        for sound_file in sound_files:
            file_path = os.path.join(self.sound_directory, sound_file)
            try:
                sound_effect = pygame.mixer.Sound(file_path)
                self.loaded_sounds[sound_file] = sound_effect
            except pygame.error as e:
                print(f"Error loading sound {sound_file}: {e}")

    def play_sound(self, sound_name: str):
        if sound_name in self.loaded_sounds:
            self.loaded_sounds[sound_name].play()
        else:
            print(f"Error: Sound '{sound_name}' not found.")

# Example Usage:
# sound_manager = SoundManager("path/to/sounds")
# sound_manager.load_sound_effects(["shoot.wav", "explode.wav"])
# sound_manager.play_sound("shoot.wav")
```
