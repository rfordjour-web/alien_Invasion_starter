from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Game window title 
        self.name = "Alien Invasion"

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = str(Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png')

        # Ship settings
        self.ship_file = str(Path.cwd() / 'Assets' / 'images'/ 'ship2(no bg).png')
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 5
        self.starting_ship_count = 3  

        # Bullet settings
        self.bullet_file = str(Path.cwd() / 'Assets' / 'images' / 'laserBlast.png')
        self.laser_sound = str(Path.cwd() / 'Assets' / 'sound' / 'laser.mp3')
        self.impact_sound = str(Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3')
        self.bullet_speed = 7
        self.bullet_width = 5
        self.bullet_height = 80
        self.bullet_amount = 5

        # Alien settings
        self.alien_file = str(Path.cwd() / 'Assets' / 'images' / 'enemy_4.png')
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_speed = 2
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.fleet_drop_speed = 40
