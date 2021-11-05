# intruder
import pygame
from pygame.sprite import Sprite

# Alyaesub means Intruder in Arabic and is based on the Harkonnen from Dune
class Dakhil(Sprite):
    """A class to represent a single Dakhil frigate in the fleet."""

    def __init__(self, ai_game):
        """Initialize the Dakhil and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the Dakhil 8 bit image and set its rect attribute.
        self.image = pygame.image.load('assets/imgs/bad_guy.bmp')
        self.rect = self.image.get_rect()

        # Start each new Dakhil near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):
        """Return True if Dakhil is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the dakhil to the right."""
        self.x += (self.settings.dakhil_speed *
                   self.settings.dakhil_direction)
        # Store the dakhil's exact horizontal position.
        self.rect.x = float(self.x)


class CreateFleet(Sprite):
    def __init__(self, ai_game, alyaesub):
        super().__init__()
        self.ai_game = ai_game
        self.alyaesub = alyaesub
        self.dakhils = pygame.sprite.Group()
        self.settings = ai_game.settings
        self._create_fleet()

    def draw(self, screen):
        self.dakhils.draw(screen)

    def _create_dakhil(self, dakhil_number, row_number):
        """Create an Dakhil frigate and place it in the row."""
        dakhil = Dakhil(self.ai_game)
        dakhil_width, dakhil_height = dakhil.rect.size
        dakhil.x = dakhil_width + 2.15 * dakhil_width * dakhil_number
        dakhil.rect.x = dakhil.x
        dakhil.rect.y = dakhil.rect.height + 1 * dakhil.rect.height * row_number
        self.dakhils.add(dakhil)

    def update_dakhils(self):
        """Check if the fleet is at an edge, then update the positions of all dakhil frigates in the fleet."""
        self._check_fleet_edges()
        self.dakhils.update()

        # Check for any bullets that have hit dakhil.
        #   If so, get rid of the bullet and the dakhil.

        # collisions = pygame.sprite.groupcollide(
        #     self.bullets, self.dakhil, True, True)

    def _check_fleet_edges(self):
        """Respond appropriately if any Dakhils have reached an edge."""
        for dakhil in self.dakhils.sprites():
            if dakhil.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for dakhil in self.dakhils.sprites():
            dakhil.rect.y += self.settings.fleet_drop_speed
        self.settings.dakhil_direction *= -1

    def _create_fleet(self):
        """Create the fleet of Dakhil frigates."""
        # Spacing between each Dakhil is equal to....  .
        # Make an dakhil.
        dakhil = Dakhil(self.ai_game)
        dakhil_width = dakhil.rect.width
        dakhil_width, dakhil_height = dakhil.rect.size
        available_space_x = self.settings.screen_width - (3 * dakhil_width)
        number_dakhils_x = available_space_x // (2 * dakhil_width)

        # Determine the number of rows of Dakhil frigates that fit on the screen.
        alyaesub_height = self.alyaesub.rect.height

        available_space_y = (self.settings.screen_height -
                             (3 * dakhil_height) - alyaesub_height)
        number_rows = available_space_y // (1 * dakhil_height)

        # Create the full fleet of Dakhil frigates.
        for row_number in range(number_rows):
            for dakhil_number in range(number_dakhils_x):
                self._create_dakhil(dakhil_number, row_number)
