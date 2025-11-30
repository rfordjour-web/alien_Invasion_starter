




from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # ------------------------
        # Game window title
        # ------------------------
        self.name = "Alien Invasion"

        # ------------------------
        # Screen settings
        # ------------------------
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60

        # ------------------------
        # Ship settings
        # ------------------------
        self.ship_file = str(Path.cwd() / 'Assets' / 'images'/ 'ship2(no bg).png')
        self.ship_width = 40
        self.ship_height = 60
        self.ship_speed = 5
        self.starting_ship_count = 5  # start with 5 lives

        # ------------------------
        # Bullet settings
        # ------------------------
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.bullet_color = (255, 255, 255)
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_amount = 5

        # ------------------------
        # Alien settings
        # ------------------------
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_width = 40
        self.alien_height = 40
        self.fleet_speed = 2
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.fleet_drop_speed = 40

        # ------------------------
        # Alien drum intro
        # ------------------------
        self.alien_drums = Path.cwd() / 'Assets' / 'sound'/'alien_drums.wav'
