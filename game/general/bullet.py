# Pew pew
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, direction):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.direction = direction
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = self.ai_game.ship.rect.midtop
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    # Checks if player shot, or intruder
    def update(self):
        if self.direction == "left":
            self.rect.x -= 1
        elif self.direction == "right":
            self.rect.x += 1

        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
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
        self.bullets_fired = 0

    def draw(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def fire_bullet(self):
        directions = ["left", "center", "right"]

        if self.ai_game.stats.power_up_active:
            for direction in directions:
                self.create_single_bullet(direction)
        else:
            self.create_single_bullet("center")

    def create_single_bullet(self, direction):
        """Create a new bullet and add it to the bullets group."""
        if not self.ai_game.stats.power_up_active:
            if self.bullets_fired < self.settings.bullets_allowed:
                new_bullet = Bullet(self.ai_game, direction)
                self.bullets.add(new_bullet)
                self.bullets_fired += 1

        else:
            new_bullet = Bullet(self.ai_game, direction)
            self.bullets.add(new_bullet)

    def remove_bullet(self, bullet):
        if not self.bullets_fired < 0:
            self.bullets_fired -= 1

        self.bullets.remove(bullet)

    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.remove_bullet(bullet)
            elif bullet.rect.left <= 0:
                self.remove_bullet(bullet)
            elif bullet.rect.right >= self.ai_game.screen.get_width():
                self.remove_bullet(bullet)


        self._check_bullet_collisions()

    def _check_bullet_collisions(self):
        """Respond to bullet-Alien collisions."""
        # Remove any bullets and Alien that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                # The level scroe multiplier does not work on the first level
                level = 1
                if not self.ai_game.stats.power_up_active:
                    self.bullets_fired -= 1


                if self.ai_game.stats.level > 0:
                    level = self.ai_game.stats.level

                self.ai_game.stats.score += (5 * self.settings.score_multiplier*level) * len(aliens)
                self.ai_game.stats.enemies_slain += 1
                self.ai_game.sb.prep_score()

            if self.ai_game.stats.score >= self.ai_game.stats.high_score:
                self.ai_game.stats.high_score = self.ai_game.stats.score
                self.ai_game.sb.prep_score()

        if not self.ai_game.aliens.aliens:
            self.ai_game.stats.level_up()
            self.ai_game.sb.prep_score()
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.aliens.create_fleet()
