






import sys
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import ShipArsenal
from alien_fleet import AlienFleet

class AlienInvasion:
    """Main class to manage game assets and behavior."""
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.name)

        self.clock = pygame.time.Clock()
        self.running = True

        # Game stats
        self.game_stats = GameStats(self.settings.starting_ship_count)

        # Ship and arsenal
        self.ship = Ship(self)

        # Alien fleet
        self.alien_fleet = AlienFleet(self)

        # Play alien drum intro
        self.play_alien_drums()

        # Font for life counter
        self.font = pygame.font.SysFont(None, 40)

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

        # Black star
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
    # Play alien drum intro
    # ------------------------
    def play_alien_drums(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.settings.alien_drums)
            pygame.mixer.music.play(-1)

    # ------------------------
    # Draw lives counter
    # ------------------------
    def draw_lives(self):
        lives_text = f"Lives: {self.game_stats.ships_left}"
        color = (255, 255, 255)
        # Warning color if <=2 lives
        if self.game_stats.ships_left <= 2:
            color = (255, 0, 0)
        text_surf = self.font.render(lives_text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.topright = (self.settings.screen_width - 20, 20)
        self.screen.blit(text_surf, text_rect)

    # ------------------------
    # Game loop
    # ------------------------
    def run_game(self):
        while self.running:
            self._check_events()

            if self.game_stats.ships_left > 0:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
                self._update_screen()

            self.clock.tick(self.settings.FPS)

    # ------------------------
    # Check collisions
    # ------------------------
    def _check_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal, self.alien_fleet.fleet, True, True
        )
        if collisions:
            # Play impact sound
            pygame.mixer.Sound(self.settings.impact_sound).play()

        if self.alien_fleet.check_fleet_bottom():
            self._ship_hit()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    # ------------------------
    # Ship gets hit
    # ------------------------
    def _ship_hit(self):
        self.game_stats.ships_left -= 1
        if self.game_stats.ships_left > 0:
            self._reset_level()
            sleep(0.5)
        else:
            self.running = False  # Game over

    # ------------------------
    # Reset level
    # ------------------------
    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.play_alien_drums()

    # ------------------------
    # Update screen
    # ------------------------
    def _update_screen(self):
        self.draw_ghana_background()
        self.ship.draw()
        self.alien_fleet.draw()
        self.draw_lives()
        pygame.display.flip()

    # ------------------------
    # Event handling
    # ------------------------
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown(event)
            elif event.type == pygame.KEYUP:
                self._keyup(event)

    def _keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
