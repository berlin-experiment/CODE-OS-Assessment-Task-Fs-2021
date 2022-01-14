import pygame
from pygame.sprite import Sprite
import random
from threading import Timer


class PowerUp(Sprite):
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen.get_rect()
        self.screen.width = self.screen.right - self.screen.left

        # Keep track of the reseting position if the player missed the timeout
        self.has_reset = False

        # self.screen.height = self.screen.top - self.screen.bottom

        self.settings = ai_game.settings
        # Load the harkonnen 8 bit image and set its rect attribute.
        self.image = pygame.image.load('game/assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new harkonnen near the top left of the screen.
        self.rect.x = random.randint(0, self.screen.width - self.rect.width)
        self.rect.y = - self.rect.height

    def check_edges(self):
        """Return True if harkonnen is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def check_for_player_collision(self):
        if pygame.sprite.spritecollideany(self.ai_game.ship, self.ai_game.power_up):
            self.ai_game.stats.activate_power_up()

            # Remove power up sprite from screen
            self.ai_game.power_up.empty()

            # Add a timer to remove power up buff

            t1 = Timer(self.settings.power_up_timer, self.remove_power_up_buff)
            t1.start()

            # Wait before spawning a new sprite
            timeout = self.ai_game.settings.power_up_timer + random.randint(10, 15)
            t2 = Timer(timeout, self.add_new_power_up)
            # Start timer
            t2.start()

    # Add new sprite to sprite group
    def add_new_power_up(self):
        self.ai_game.power_up.add(self.ai_game.p_u)

    def remove_power_up_buff(self):
        self.ai_game.bullets.bullets_fired = 0
        self.ai_game.stats.deactivate_power_up()

    def reset_p_u_position(self):
        self.rect.y = - self.rect.height
        self.rect.x = random.randint(0, self.screen.width - self.rect.width)
        self.has_reset = False

    def update(self):
        """Move the alien to the right."""
        if self.rect.y >= self.screen.height + self.rect.height and not self.has_reset:
            t3 = Timer(random.randint(0, 10), self.reset_p_u_position)
            self.has_reset = True

            t3.start()
        else:
            self.rect.y += 2
        self.check_for_player_collision()






