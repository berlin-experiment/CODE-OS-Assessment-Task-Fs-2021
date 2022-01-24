from .default_settings import DefaultSettings

default_settings = DefaultSettings()


class Settings:
    """Class to store Alrimal Game settings"""
    def __init__(self, screen):
        self.screen = screen
        self.restore_default_settings()

    def restore_default_settings(self):
        # These settings are loaded as initial values, and are dynamic (change with game state)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_color = default_settings.bg_color

        # Ship settings
        self.ship_speed = default_settings.ship_speed
        self.ship_limit = default_settings.ship_limit

        # Bullet settings
        self.bullet_speed = default_settings.bullet_speed
        self.bullet_width = default_settings.bullet_width
        self.bullet_height = default_settings.bullet_height
        self.bullet_color = default_settings.bullet_color
        self.bullets_allowed = default_settings.bullets_allowed

        # Alien  settings
        self.alien_speed = default_settings.alien_speed
        self.fleet_drop_speed = default_settings.fleet_drop_speed
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = default_settings.fleet_direction
        self.alien_direction = default_settings.alien_direction

        # flap count
        self.flapcount = default_settings.flapcount

        # Score multiplier that increases the level point gain
        self.score_multiplier = default_settings.score_multiplier

        # Power up timer
        self.power_up_timer = default_settings.power_up_timer
