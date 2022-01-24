import pygame
from pygame.sprite import Sprite
import random


class Background(Sprite):
    """A class to create the game's backgound"""
    def __init__(self, ai_game):
        """Initialize the background and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen.get_rect()
        self.screen.width = self.screen.right - self.screen.left
        self.settings = ai_game.settings
        # Load the background 8 bit image and set its rect attribute.
        # Super crap dirt drawing I made using PhotoScape X
        self.image = pygame.image.load('game/assets/floor.bmp')
        self.rect = self.image.get_rect()
        # Starting position of the background image is random
        self.rect.x = random.randint(0, self.screen.width - self.rect.width)
        self.rect.y = - self.rect.height

    def check_edges(self):
        """Keep the background animation within screen view"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the background to the bottom."""
        if self.rect.y >= self.screen.height + self.rect.height:
            self.rect.y = - self.rect.height
            self.rect.x = random.randint(0, self.screen.width - self.rect.width)
        else:
            self.rect.y += 1
