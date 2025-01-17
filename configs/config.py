# Space Bugs Game Configuration

# Screen dimensions
SCREEN_WIDTH: int = 800     # Width of the game screen in pixels
SCREEN_HEIGHT: int = 600    # Height of the game screen in pixels
MAX_ENEMIES: int = 8

# Player settings
PLAYER_SPEED: float = 5.0   # Movement speed of the player's ship
PLAYER_SIZE: tuple[int, int] = (200, 200)  # Dimensions of the player's ship defined by width and height in pixels

# Enemy settings
ENEMY_SPEED: float = 3.0    # Movement speed of the enemy ships

# Bullet settings
BULLET_SPEED: float = 10.0  # Speed of bullets fired by player
ENEMY_BULLET_SPEED: float = 7.0 # Speed of bullets fired by enemies

# Game loop settings
FPS: int = 60               # Frames per second for the game loop

# Game configuration attributes
WIDTH: int = 600
HEIGHT: int = 400
BLOCK_SIZE: int = 10
SNAKE_SPEED: int = 15
FONT_SIZE: int = 24