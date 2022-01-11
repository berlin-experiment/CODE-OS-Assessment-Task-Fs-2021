# Pew pew
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, shooter):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.shooter = shooter

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    # Checks if player shot, or intruder
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        if self.shooter == 'player':
            self.y -= self.settings.bullet_speed
            # Update the rect position.
            self.rect.y = self.y
        else:
            self.y += self.settings.bullet_speed
            # Update the rect position.
            self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class PewPew:
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.ship = ai_game.ship
        self.aliens = ai_game.aliens
        self.bullets = pygame.sprite.Group()

    def draw(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def fire_bullet(self, shooter=''):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.ai_game, shooter)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        """Respond to bullet-Alien collisions."""
        # Remove any bullets and Alien that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens.aliens, True, True)

        if not self.ai_game.aliens.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.aliens._create_fleet()

        # # checking for player-bullet collision
        # collisions = pygame.sprite.groupcollide(
        #     self.bullets, self.ship, True, True)
        #
        # if not self.ship:
        #     # Destroy existing bullets and create new fleet.
        #     self.ai_game.reduce_health()

# still need to do
# Both player and alien must shoot
