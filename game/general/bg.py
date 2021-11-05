import pygame
from pygame.sprite import Sprite
import random


class Background(Sprite):
    """A class to represent a single harkonnen frigate in the fleet."""

    def __init__(self, ai_game):
        """Initialize the harkonnen and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen.get_rect()
        self.screen.width = self.screen.right - self.screen.left

        # self.screen.height = self.screen.top - self.screen.bottom

        self.settings = ai_game.settings
        # Load the harkonnen 8 bit image and set its rect attribute.
        self.image = pygame.image.load('assets/imgs/ground_floor.bmp')
        self.rect = self.image.get_rect()

        # Start each new harkonnen near the top left of the screen.
        self.rect.x = random.randint(0, self.screen.width - self.rect.width)
        self.rect.y = - self.rect.height

    def check_edges(self):
        """Return True if harkonnen is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right."""
        if self.rect.y >= self.screen.height + self.rect.height:
            self.rect.y = - self.rect.height
            self.rect.x = random.randint(0, self.screen.width - self.rect.width)
        else:
            self.rect.y += 1
