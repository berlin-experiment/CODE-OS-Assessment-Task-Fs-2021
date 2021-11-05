import sys
import pygame

from .general.settings.settings import Settings
from .general.bg import Background
from .player.alyaesub import Alyaesub
from .intruders.dakhil import CreateFleet
from .general.bullet import PewPew


# Alrimal means the Sandy in Arabic and is based on the Ornithopter from Dune
class AlrimalGame:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources... or so they say"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("CODE Assessment Game")
        # Create background
        self.bg = Background(self)
        self.Background = pygame.sprite.Group()
        self.Background.add(self.bg)
        # creating player
        self.alyaesub = Alyaesub(self)
        # creating enemy fleet
        self.dakhils = CreateFleet(self, self.alyaesub)
        # creating bullet
        self.bullets = PewPew(self)

    # doesn't work properly yet...
    def reduce_health(self):
        sys.exit()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.bg.update()
            self.bullets.update_bullets()
            self.alyaesub.update()
            self.dakhils.update_dakhils()
            self._update_screen()

    def _check_events(self):
        """Respond to key press and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key press"""
        if event.key == pygame.K_RIGHT:
            self.alyaesub.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.alyaesub.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bullets.fire_bullet('player')

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.alyaesub.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.alyaesub.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.Background.draw(self.screen)
        self.dakhils.draw(self.screen)
        self.bullets.draw()
        self.alyaesub.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
