import pygame.font

"""A class to report scoring information."""


class Scoreboard:
    """Initialize scorekeeping attributes."""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
    # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.score_font = pygame.font.SysFont(None, 48)
        self.level_font = pygame.font.SysFont(None, 48)
        self.lives_left_font = pygame.font.SysFont(None, 48)

        self.score_image = None
        self.score_rect = None
        self.level_image = None
        self.level_rect = None
        self.lives_left_image = None
        self.lives_left_rect = None
        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = "Score: " + str(self.stats.score)
        level_str = "Lvl: " + str(self.stats.level)
        lives_str = "Lives Left: " + str(self.stats.ships_left)

        self.score_image = self.score_font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        self.level_image = self.level_font.render(level_str, True,
                                                  self.text_color, self.settings.bg_color)

        self.lives_left_image = self.lives_left_font.render(lives_str, True,
                                                  self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # Display the level at the top left of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = 20

        # Display the lives left at the top left of the screen.
        self.lives_left_rect = self.lives_left_image.get_rect()
        self.lives_left_rect.left = self.screen_rect.left + 20
        self.lives_left_rect.top = 60

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.lives_left_image, self.lives_left_rect)





