import pygame


class SoundManager:
    MOVE_SOUND: str = "sounds/move.mp3"
    SHOOT_SOUND: str = "sounds/shoot.mp3"
    BGM_SOUND: str = "sounds/bgm.mp3"
    EXPLOSION_SOUND: str = "sounds/explosion.mp3"
    GAME_OVER: str = "sounds/game_over.mp3"

    def __init__(self):
        self.sound_files = [
            SoundManager.MOVE_SOUND,
            SoundManager.SHOOT_SOUND,
            SoundManager.BGM_SOUND,
            SoundManager.EXPLOSION_SOUND,
            SoundManager.GAME_OVER
        ]
        self.loaded_sounds = {}

    def load_sounds(self) -> None:
        pygame.mixer.init()
        """Load sound files using pygame and store them in the loaded_sounds dictionary."""
        for path in self.sound_files:
            self.loaded_sounds[path] = pygame.mixer.Sound(path)

    def play_sound(self, sound_name: str, loop: bool = False) -> None:
        """Play a sound by name. Loop indefinitely if loop is True, else play once."""
        sound = self.loaded_sounds[sound_name]
        loops = -1 if loop else 0
        sound.stop()
        sound.play(loops=loops)
