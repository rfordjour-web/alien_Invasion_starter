import sys
import pygame
from time import sleep

# ------------------------
# Minimal Settings
# ------------------------
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.name = "Alien Invasion"
        self.FPS = 60
        self.bullets_amount = 3

# ------------------------
# Dummy Bullet class
# ------------------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 5, 10)

    def update(self):
        self.rect.y -= 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

# ------------------------
# Dummy Ship class
# ------------------------
class Ship:
    def __init__(self, game):
        self.game = game
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.rect = pygame.Rect(400, 500, 50, 50)
        self.arsenal = pygame.sprite.Group()

    def update(self):
        if self.moving_right:
            self.rect.x += 5
        if self.moving_left:
            self.rect.x -= 5
        if self.moving_up:
            self.rect.y -= 5
        if self.moving_down:
            self.rect.y += 5

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 255), self.rect)

# ------------------------
# Dummy AlienFleet
# ------------------------
class AlienFleet:
    def __init__(self, game):
        self.game = game
        self.fleet = pygame.sprite.Group()
        self.create_fleet()

    def create_fleet(self):
        for i in range(5):
            alien = pygame.Rect(100*i + 50, 50, 40, 40)
            self.fleet.add(alien)

    def update_fleet(self):
        pass

    def draw(self):
        for alien in self.fleet:
            pygame.draw.rect(self.game.screen, (255, 0, 0), alien)

# ------------------------
# Main Game Class
# ------------------------
class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()

        # ------------------------
        # Alien drum sound
        # ------------------------
        self.alien_drums = 'Assets/alien_drums.wav'

        self.ship = Ship(self)
        self.alien_fleet = AlienFleet(self)

    # ------------------------
    # Ghana flag background
    # ------------------------
    def draw_ghana_background(self):
        screen_w = self.settings.screen_width
        screen_h = self.settings.screen_height
        stripe_h = screen_h // 3

        RED = (206, 17, 38)
        GOLD = (252, 209, 22)
        GREEN = (0, 122, 61)
        BLACK = (0, 0, 0)

        pygame.draw.rect(self.screen, RED, (0, 0, screen_w, stripe_h))
        pygame.draw.rect(self.screen, GOLD, (0, stripe_h, screen_w, stripe_h))
        pygame.draw.rect(self.screen, GREEN, (0, stripe_h*2, screen_w, stripe_h))

        star_size = stripe_h // 2
        center_x = screen_w // 2
        center_y = stripe_h + (stripe_h // 2)

        star_points = [
            (center_x, center_y - star_size // 2),
            (center_x + star_size // 3, center_y - star_size // 8),
            (center_x + star_size // 2, center_y - star_size // 8),
            (center_x + star_size // 4, center_y + star_size // 6),
            (center_x + star_size // 3, center_y + star_size // 2),
            (center_x, center_y + star_size // 3),
            (center_x - star_size // 3, center_y + star_size // 2),
            (center_x - star_size // 4, center_y + star_size // 6),
            (center_x - star_size // 2, center_y - star_size // 8),
            (center_x - star_size // 3, center_y - star_size // 8),
        ]
        pygame.draw.polygon(self.screen, BLACK, star_points)

    # ------------------------
    # Play alien drum safely
    # ------------------------
    def play_alien_drums(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.alien_drums)
            pygame.mixer.music.play(-1)

    # ------------------------
    # Run game loop
    # ------------------------
    def run_game(self):
        # Play drum once at start
        self.play_alien_drums()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.draw_ghana_background()
            self.ship.draw()
            self.alien_fleet.draw()
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)

# ------------------------
# Run the game
# ------------------------
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()





