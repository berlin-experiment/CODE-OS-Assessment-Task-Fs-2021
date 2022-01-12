import sys
import pygame
import pygame.font

from time import sleep

from .general.settings.settings import Settings
from .general.game_stats import GameStats
from .general.bg import Background
from .player.ship import Ship
from .intruders.alien import CreateFleet
from .general.bullet import PewPew
from .general.scoreboard import Scoreboard


# Alrimal means the Sandy in Arabic and is based on the Ornithopter from Dune
class AlrimalGame:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources... or so they say"""
        pygame.init()
        pygame.font.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("CODE Assessment Game")
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        # Create background
        self.bg = Background(self)
        self.Background = pygame.sprite.Group()
        self.Background.add(self.bg)
        # creating player
        self.ship = Ship(self)
        # creating enemy fleet
        self.aliens = CreateFleet(self, self.ship)
        # creating bullet
        self.bullets = PewPew(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.bg.update()
            self.bullets.update_bullets()
            self.ship.update()
            self.aliens.update_aliens()
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
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.bullets.fire_bullet('player')

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        if self.stats.ships_left >= 0:
            self.screen.fill(self.settings.bg_color)
            self.Background.draw(self.screen)
            self.aliens.draw(self.screen)
            self.bullets.draw()
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            self.sb.show_score()
            pygame.display.flip()


