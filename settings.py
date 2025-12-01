



from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):

        # ------------------------
        # Game window
        # ------------------------
        self.name = "Alien Invasion"

        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60

        # ------------------------
        # Ship settings
        # ------------------------
        self.ship_file = str(Path.cwd() / "Assets" / "images" / "ship2(no bg).png")
        self.ship_width = 30
        self.ship_height = 44
        self.ship_speed = 7
        self.starting_ship_count = 5

        # ------------------------
        # Bullet settings
        # ------------------------
        self.bullet_width = 7
        self.bullet_height = 25
        self.bullet_speed = 12
        self.bullets_allowed = 10
        self.bullet_color = (255, 255, 255)

        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "impactSound.mp3"

        # ------------------------
        # Alien settings
        # ------------------------
        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.alien_width = 40
        self.alien_height = 40

        self.fleet_speed = 0.5
        self.fleet_direction = 1
        self.fleet_drop_speed = 25

        # ------------------------
        # Sound
        # ------------------------
        self.alien_drums = Path.cwd() / "Assets" / "sound" / "alien_drums.wav"
