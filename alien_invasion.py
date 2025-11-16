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
        self.clock = pygame.time.Clock()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (
            self.settings.screen_width, self.settings.screen_height)
            )
        self.clock = pygame.time.Clock()



        self.running = True

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while self.running:
            self._check_events()    
            self.ship.update()  # Update the ship's position
            self._update_screen() # Update the screen
            self.clock.tick(self.settings.FPS)  # Limit the frame rate to 60 FPS
    

               
        

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
            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)   
            elif  event.type == pygame.KEYUP:
               self._check_keyup_events(event)   

              
                    
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        ...
    
    def run_game(self):
        ...
    
    def _update_screen(self):
        ...
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()            # Redraw the screen during each pass through the loop
