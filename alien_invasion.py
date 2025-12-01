





import sys
import math
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien_fleet import AlienFleet

# ------------------------
# Decorative star
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


class AlienInvasion:
    """Main game class."""

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

        # Player ship
        self.ship = Ship(self)

        # Alien fleet
        self.alien_fleet = AlienFleet(self)

        # Fonts
        self.font = pygame.font.SysFont(None, 44)
        self.menu_font = pygame.font.SysFont(None, 56)
        self.title_font = pygame.font.SysFont(None, 90)

        # ----------------
        # MENU STATE
        # ----------------
        self.show_menu = True
        self.menu_options = list(self.settings.difficulties.keys())
        self.menu_index = 0

        self._play_drums()

    # ------------------------
    # Play background drums
    # ------------------------
    def _play_drums(self):
        try:
            pygame.mixer.music.load(self.settings.alien_drums)
            pygame.mixer.music.play(-1)
        except:
            print("⚠️ Couldn't load drums sound")

    # ------------------------
    # DRAW DIFFICULTY MENU
    # ------------------------
    def draw_menu(self):

        self.screen.fill((0, 0, 0))

        # Ghana gold
        GOLD = (252, 209, 22)

        title_text = self.title_font.render("ALIENS vs GHANA 🇬🇭", True, GOLD)
        self.screen.blit(
            title_text,
            (self.settings.screen_width // 2 - title_text.get_width() // 2, 120)
        )

        for i, option in enumerate(self.menu_options):

            if i == self.menu_index:
                color = (0, 255, 0)
                label = f">> {option}"
            else:
                color = (255,255,255)
                label = option

            text = self.menu_font.render(label, True, color)

            self.screen.blit(
                text,
                (self.settings.screen_width // 2 - text.get_width() // 2,
                 300 + i * 65)
            )

        hint = self.font.render("Use ↑ ↓ to choose    ENTER to start", True, (180,180,180))
        self.screen.blit(
            hint,
            (self.settings.screen_width //2 - hint.get_width()//2, 550)
        )

        pygame.display.flip()

    # ------------------------
    # GAME LOOP
    # ------------------------
    def run_game(self):

        while self.running:

            self._check_events()

            if self.show_menu:
                self.draw_menu()
                continue

            # Run game normally
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

        pygame.sprite.groupcollide(
            self.ship.arsenal.arsenal,
            self.alien_fleet.fleet,
            True,
            True
        )

        if self.alien_fleet.check_fleet_bottom():
            self._ship_hit()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    # ------------------------
    # Player hit
    # ------------------------
    def _ship_hit(self):

        self.game_stats.ships_left -= 1

        if self.game_stats.ships_left > 0:
            self._reset_level()
            sleep(0.6)
        else:
            pygame.quit()
            sys.exit()

    # ------------------------
    # Reset level
    # ------------------------
    def _reset_level(self):

        self.ship.arsenal.arsenal.empty()

        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    # ------------------------
    # Refresh screen
    # ------------------------
    def _update_screen(self):

        self.screen.fill((10,10,10))

        self.ship.draw()
        self.alien_fleet.draw()

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

    # ------------------------
    # Key down
    # ------------------------
    def _keydown(self, event):

        if self.show_menu:

            if event.key == pygame.K_UP:
                self.menu_index = (self.menu_index - 1) % len(self.menu_options)

            elif event.key == pygame.K_DOWN:
                self.menu_index = (self.menu_index + 1) % len(self.menu_options)

            elif event.key == pygame.K_RETURN:
                choice = self.menu_options[self.menu_index]
                self.settings.current_difficulty = choice
                self.settings.apply_difficulty()

                self.show_menu = False
                self.alien_fleet.create_fleet()

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        else:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                self.ship.fire()

            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # ------------------------
    # Key up
    # ------------------------
    def _keyup(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":

    game = AlienInvasion()
    game.run_game()
