
class GameStats:
    """Initialize statistics that can change during the game."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.ai_game = ai_game
        self.reset_stats()
        self.high_score = 0
        self.power_up_active = False
        # Start Alien Invasion in an non-active state.
        self.game_active = False

    def reset_stats(self):
        self.ai_game.ship.center_ship()
        self.ai_game.settings.restore_default_settings()
        self.settings = self.ai_game.settings
        self.level = 0
        self.score = 0
        self.enemies_slain = 0
        self.ships_left = self.ai_game.settings.ship_limit

    def level_up(self):
        # If the game is active, increase the settings
        if self.game_active:
            self.ai_game.settings.ship_speed += 0.5
            self.ai_game.settings.alien_speed += 0.5
            self.ai_game.settings.fleet_drop_speed += 2
            self.ai_game.settings.bullet_speed = 1.5
            self.level = self.level + 1
            self.score += self.level * 100
            self.ai_game.bullets.bullets_fired = 0

        # Check to see if the high score has been beat
        if self.ai_game.stats.score >= self.ai_game.stats.high_score:
            self.ai_game.stats.high_score = self.ai_game.stats.score
            self.ai_game.sb.prep_score()

    def activate_power_up(self):
        self.power_up_active = True

    def deactivate_power_up(self):
        self.power_up_active = False
