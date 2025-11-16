import sys
import pygame
from settings import Settings 
from ship import Ship






class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (
            self.settings.screen_width, self.settings.screen_height)
            )



        self.running = True

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while self.running:
            
            self._check_events()

            self._update_screen() # Update the screen
            self.clock = pygame.time.Clock() 

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))   # Draw the background image to the screen    
        self.ship.draw()  # Draw the ship at its current location 
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit() # Limit the frame rate to 60 FPS



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()            # Redraw the screen during each pass through the loop
