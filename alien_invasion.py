





import sys
import math
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien_fleet import AlienFleet

# ------------------------
# Star geometry utility
# ------------------------
def draw_star(surface, color, center, radius):
    points = []
    for i in range(10):
        angle = math.radians(90 - i * 36)
        r = radius if i % 2 == 0 else radius * 0.4
        x = center[0] + r * math.cos(angle)
        y = center[1] - r * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

# ------------------------
# Lens flare rays
# ------------------------
def draw_starburst(surface, color, center, radius, ray_len, count):
    for i in range(count):
        angle = math.radians((360 / count) * i)
        x1 = center[0] + math.cos(angle) * radius
        y1 = center[1] + math.sin(angle) * radius
        x2 = center[0] + math.cos(angle) * (radius + ray_len)
        y2 = center[1] + math.sin(angle) * (radius + ray_len)
        pygame.draw.line(surface, color, (x1, y1), (x2, y2), 2)

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

        # Ship
        self.ship = Ship(self)

        # Alien fleet
        self.alien_fleet = AlienFleet(self)

        # Font
        self.font = pygame.font.SysFont(None, 40)

        # FX timers
        self.star_timer = 0
        self.ripple_timer = 0

        # Drum beat timing
        self.beat_max = 40
        self.beat_timer = self.beat_max

        # Win celebration
        self.win_flash_timer = 0
        self.win_flash_duration = 60
        self.win_flash_active = False

        self.play_alien_drums()

    # ------------------------
    # Ghana FX background
    # ------------------------
    def draw_ghana_background(self):
        w = self.settings.screen_width
        h = self.settings.screen_height
        stripe_h = h // 3

        RED   = (206, 17, 38)
        GOLD  = (252, 209, 22)
        GREEN = (0, 122, 61)
        BLACK = (0, 0, 0)

        # Ripple effect synced to beat
        self.ripple_timer += 1
        if self.beat_timer >= self.beat_max:
            self.beat_timer = 0
            self.ripple_timer = 0
        else:
            self.beat_timer += 1

        ripple_radius = self.ripple_timer * 10
        ripple_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        if ripple_radius < w:
            pygame.draw.circle(
                ripple_surface,
                (255, 215, 60, 40),
                (w//2, h//2),
                ripple_radius,
                6
            )

        pygame.draw.rect(self.screen, RED,   (0, 0, w, stripe_h))
        pygame.draw.rect(self.screen, GOLD,  (0, stripe_h, w, stripe_h))
        pygame.draw.rect(self.screen, GREEN, (0, stripe_h*2, w, stripe_h))

        self.screen.blit(ripple_surface, (0, 0))

        # Pulsing star glow
        self.star_timer += 0.07
        pulse = math.sin(self.star_timer) * 5

        cx = w // 2
        cy = stripe_h + (stripe_h // 2)
        base_radius = stripe_h * 0.35
        radius = base_radius + pulse

        # Lens flare rays
        draw_starburst(
            self.screen,
            (255, 215, 90),
            (cx, cy),
            radius,
            ray_len=46 + abs(pulse * 3),
            count=12
        )

        # Soft glow
        draw_star(self.screen, (60, 60, 60), (cx, cy), radius + 6)

        # Main star
        draw_star(self.screen, BLACK, (cx, cy), radius)

    # ------------------------
    # Drum intro
    # ------------------------
    def play_alien_drums(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.settings.alien_drums)
            pygame.mixer.music.play(-1)

    # ------------------------
    # Lives UI
    # ------------------------
    def draw_lives(self):
        lives_text = f"Lives: {self.game_stats.ships_left}"
        color = (255, 255, 255)
        if self.game_stats.ships_left <= 2:
            color = (255, 0, 0)
        text_surf = self.font.render(lives_text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.topright = (self.settings.screen_width - 20, 20)
        self.screen.blit(text_surf, text_rect)

    # ------------------------
    # Win celebration
    # ------------------------
    def draw_win_flash(self):
        if self.win_flash_active:
            flash_surface = pygame.Surface(
                (self.settings.screen_width, self.settings.screen_height), pygame.SRCALPHA
            )
            alpha = 150 * (1 - self.win_flash_timer / self.win_flash_duration)
            flash_surface.fill((255, 255, 255, int(alpha)))
            self.screen.blit(flash_surface, (0, 0))
            self.win_flash_timer += 1
            if self.win_flash_timer >= self.win_flash_duration:
                self.win_flash_active = False

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
    # Collisions
    # ------------------------
    def _check_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal,
            self.alien_fleet.fleet,
            True,
            True
        )
        if collisions:
            pygame.mixer.Sound(self.settings.impact_sound).play()

        if self.alien_fleet.check_fleet_bottom():
            self._ship_hit()

        if self.alien_fleet.check_destroyed_status():
            self.win_flash_active = True
            self.win_flash_timer = 0
            self._reset_level()

    # ------------------------
    # Player hit
    # ------------------------
    def _ship_hit(self):
        self.game_stats.ships_left -= 1
        if self.game_stats.ships_left > 0:
            self._reset_level()
            sleep(0.5)
        else:
            self.running = False

    # ------------------------
    # Reset level
    # ------------------------
    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.play_alien_drums()

    # ------------------------
    # Screen refresh
    # ------------------------
    def _update_screen(self):
        self.draw_ghana_background()
        self.ship.draw()
        self.alien_fleet.draw()
        self.draw_lives()
        self.draw_win_flash()
        pygame.display.flip()

    # ------------------------
    # Input handling
    # ------------------------
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
