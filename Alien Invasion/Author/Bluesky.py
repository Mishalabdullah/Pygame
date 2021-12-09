import sys


import pygame
from chacrecter import charecter

class Settings:
    # A class to store all the settings for Alien Invasion

    def __init__(self) -> None:
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (0,0,255)

class bluesky:
    def __init__(self):
        pygame.init
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("bluesky")
        self.charecter = charecter(self)
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.charecter.blitme()
        pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = bluesky()
    ai.run_game()