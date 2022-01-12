class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.level = 0
        self.score = 0
        self.ships_left = ai_game.settings.ship_limit
        self.ai_game = ai_game
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.level = 0

    def level_up(self):
        self.ai_game.settings.alien_speed += 0.5
        self.ai_game.settings.fleet_drop_speed += 10
        self.level = self.level + 1
        self.score += self.level * 100

