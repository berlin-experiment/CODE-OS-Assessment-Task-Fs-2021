# player
import pygame

# Alyaesub means dragonfly in Arabic and is based on the Ornithopter from Dune
class Alyaesub:
    """CLass to manage the alyaesub"""
    def __init__(self, ai_game):
        """Initialize the alyaesub's and set its starting position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.state = 1
        self.count = 0

        # Load the alyaesub and get its rect.
        self.image = pygame.image.load('assets/imgs/alyaesub.bmp')
        self.rect = self.image.get_rect()

        # Start each new alyaesub at the bottom center of the screen. x
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the alyaesub's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the alyaesub's position based on the movement flag."""
        if self.state:
            if self.count < self.settings.flapcount:
                self.count += 1
            else:
                self.image = pygame.image.load('assets/imgs/please_work2.bmp')
                self.state = 0
                self.count = 0
        else:
            if self.count < self.settings.flapcount:
                self.count += 1
            else:
                self.image = pygame.image.load('assets/imgs/please_work.bmp')
                self.state = 1
                self.count = 0
            # self.image = pygame.image.load('assets/imgs/please_work.bmp')
            # self.state = 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.alyaesub_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.alyaesub_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the alyaesub aircraft at its current location."""
        self.screen.blit(self.image, self.rect)


# Still need to do
# Health bar
# Collisions with intruder = DEATH
