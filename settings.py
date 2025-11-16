from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.name = "Alien Invasion"  # Removed type hint
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'starbasesnow.png'
        self.bg_color = (230, 230, 230)
        
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2.png'
        self.ship_width = 40
        self.ship_height = 60