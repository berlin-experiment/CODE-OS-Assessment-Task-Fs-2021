import pygame
from pygame.sprite import Sprite


# The aliens are based on the Harkonnen from Dune, but I just drew a stereotypical space frigate using PhotoScape X
class Alien(Sprite):
    """A class to represent a single alien frigate in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien 8 bit image and set its rect attribute.
        self.image = pygame.image.load('game/assets/bad_guy.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right."""
        self.x += (self.settings.alien_speed *
                   self.settings.alien_direction)
        # Store the alien's exact horizontal position.
        self.rect.x = float(self.x)


class CreateFleet(Sprite):
    """A class to generate and manage the fleet."""
    def __init__(self, ai_game, ship):
        super().__init__()
        self.ai_game = ai_game
        self.ship = ship
        self.aliens = pygame.sprite.Group()
        self.settings = ai_game.settings
        self.create_fleet()

    def draw(self, screen):
        self.aliens.draw(screen)

    def _create_alien(self, alien_number, row_number):
        """Create an Alien frigate and place it in the row."""
        alien = Alien(self.ai_game)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2.15 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
        self.aliens.add(alien)

    def update_aliens(self):
        """Check if the game is active before attempting an update """
        if self.ai_game.stats.game_active:
            # Check if the fleet is at an edge, then update the positions of all alien frigates in the fleet.
            self._check_fleet_edges()
            self.aliens.update()

            # Look for alien-ship collisions.
            if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self.ai_game.ship.ship_hit()

            screen_rect = self.ai_game.screen.get_rect()
            for alien in self.aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                    # Treat this the same as if the ship got hit.
                    self.ai_game.ship.ship_hit()
                    break

    def create_fleet(self):
        """Create the fleet of Alien frigates."""
        alien = Alien(self.ai_game)
        alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (3 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of Alien frigates that fit on the screen.
        ship_height = self.ship.rect.height

        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (1 * alien_height)

        # Create the full fleet of Alien frigates.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    def _check_fleet_edges(self):
        """Respond appropriately if any Aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.alien_direction *= -1
