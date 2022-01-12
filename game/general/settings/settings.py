class Settings:
    """Class to store Alrimal Game settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 165, 98)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 50
        self.bullet_height = 15
        self.bullet_color = (88, 0, 0)
        self.bullets_allowed = 13

        # Alien  settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 80
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_direction = 1

        # flap count
        self.flapcount = 3
        