import pygame
from sound_manager import SoundManager

class AssetsLoader:
    PLAYER_IMAGE_PATH: str = "images/player.png"
    ENEMY_IMAGE_PATH: str = "images/enemy.png"
    BULLET_IMAGE_PATH: str = "images/bullet.png"
    
    player_image: pygame.Surface = None
    enemy_image: pygame.Surface = None

    @staticmethod
    def load_image(image_path: str) -> pygame.Surface:
        """Loads an image file and returns it as a pygame Surface object."""
        try:
            image = pygame.image.load(image_path)
            return image.convert_alpha()  # Optimizes image with per-pixel alpha
        except pygame.error as e:
            raise SystemExit(f"Could not load image {image_path}: {e}")

    @classmethod
    def load_player_image(cls) -> pygame.Surface:
        """Uses load_image to load the player image using PLAYER_IMAGE_PATH."""
        if cls.player_image is None:
            cls.player_image = cls.load_image(cls.PLAYER_IMAGE_PATH)
        return cls.player_image

    @classmethod
    def load_enemy_image(cls) -> pygame.Surface:
        """Uses load_image to load the enemy image using ENEMY_IMAGE_PATH."""
        if cls.enemy_image is None:
            cls.enemy_image = cls.load_image(cls.ENEMY_IMAGE_PATH)
        return cls.enemy_image

    @classmethod
    def load_bullet_image(cls) -> pygame.Surface:
        """Uses load_image to load the bullet image using BULLET_IMAGE_PATH."""
        return cls.load_image(cls.BULLET_IMAGE_PATH)

class SoundAssetsLoader:
    sound_manager: SoundManager = SoundManager()

    @classmethod
    def initialize_sounds(cls, sound_files: dict):
        """Populate the sound_manager's sound_files and load sounds using the SoundManager."""
        cls.sound_manager.sound_files = sound_files
        for name, path in sound_files.items():
            cls.sound_manager.load_sound(name, path)

# Ensure other game components such as player and enemies reference
# the `assets_loader.py` for loading their associated images.
# Adjust the imports in those files accordingly.