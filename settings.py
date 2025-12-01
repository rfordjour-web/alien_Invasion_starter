



class Settings:
    """Store all settings for the game."""

    def __init__(self):

        # ----------------
        # Display
        # ----------------
        self.name = "Aliens vs Ghana 🇬🇭"
        self.FPS = 60
        self.screen_width = 1200
        self.screen_height = 800

        # ----------------
        # Ship
        # ----------------
        self.ship_speed = 4.5
        self.starting_ship_count = 3

        self.ship_width = 85
        self.ship_height = 65
        self.ship_file = "Assets/images/ship2.png"

        # ----------------
        # Bullets
        # ----------------
        self.bullets_allowed = 5

        # ----------------
        # Sounds
        # ----------------
        self.alien_drums = "sounds/drums.wav"
        self.laser_sound = "sounds/laser.wav"
        self.impact_sound = "sounds/explosion.wav"

        # ----------------
        # Alien settings
        # ----------------
        self.alien_width = 55
        self.alien_height = 48

        # ----------------
        # DIFFICULTY LEVELS
        # ----------------
        self.difficulties = {
            "EASY": {
                "fleet_speed": 1.0,
                "fleet_drop_speed": 0.25
            },
            "MEDIUM": {
                "fleet_speed": 2.0,
                "fleet_drop_speed": 0.65
            },
            "HARD": {
                "fleet_speed": 4.0,
                "fleet_drop_speed": 1.25
            }
        }

        # Default difficulty
        self.current_difficulty = "EASY"

        # Apply difficulty
        self.apply_difficulty()

    def apply_difficulty(self):
        """Apply selected difficulty to alien movement."""
        level = self.difficulties[self.current_difficulty]
        self.fleet_speed = level["fleet_speed"]
        self.fleet_drop_speed = level["fleet_drop_speed"]

