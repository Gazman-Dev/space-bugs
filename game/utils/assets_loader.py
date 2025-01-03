import pygame

class AssetsLoader:
    PLAYER_IMAGE_PATH: str = "images/player.png"
    ENEMY_IMAGE_PATH: str = "images/enemy.png"
    BULLET_IMAGE_PATH: str = "images/bullet.png"

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
        return cls.load_image(cls.PLAYER_IMAGE_PATH)

    @classmethod
    def load_enemy_image(cls) -> pygame.Surface:
        """Uses load_image to load the enemy image using ENEMY_IMAGE_PATH."""
        return cls.load_image(cls.ENEMY_IMAGE_PATH)

    @classmethod
    def load_bullet_image(cls) -> pygame.Surface:
        """Uses load_image to load the bullet image using BULLET_IMAGE_PATH."""
        return cls.load_image(cls.BULLET_IMAGE_PATH)

# Ensure other game components such as player and enemies reference
# the `assets_loader.py` for loading their associated images.
# Adjust the imports in those files accordingly.