import pygame.font


class Scoreboard:
    """A class to report scoring information."""
    # Initialize score keeping attributes.
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # Font settings for scoring information.
        self.bg_color = ai_game.settings.bg_color
        # Display the score at the top right of the screen.
        self.player_score = ScreenText(self.bg_color, "right", self.screen_rect.right - 20, 20, self.screen)
        # Display the number of slain enemies below the score.
        self.enemies_slain = ScreenText(self.bg_color, "right", self.screen_rect.right - 20, 60, self.screen)
        # Display the high score in the center of the screen
        self.high_score = ScreenText(self.bg_color, "middle", self.screen_rect.center, 20, self.screen)
        # Display the level at the top left of the screen.
        self.current_level = ScreenText(self.bg_color, "left", self.screen_rect.left + 20, 20, self.screen)
        # Display the ships left below the levels.
        self.ships_left = ScreenText(self.bg_color, "left", self.screen_rect.left + 20, 60, self.screen)
        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        # Total score
        self.player_score.update_values("Score: " + self.rounder(self.stats.score))
        # Total enemies
        self.enemies_slain.update_values("Fallen foes: " + str(self.stats.enemies_slain))
        # High score
        self.high_score.update_values("High score: " + self.rounder(self.stats.high_score))
        # Current level
        self.current_level.update_values("Lvl: " + str(self.stats.level))

        if self.stats.ships_left >= 0:
            self.ships_left.update_values("Lives Left: " + str(self.stats.ships_left))
        else:
            self.ships_left.update_values("You're dead Loser!")

    def show_score(self):
        """Draw score to the screen."""
        self.player_score.show_text()
        self.enemies_slain.show_text()
        self.high_score.show_text()
        self.current_level.show_text()
        self.ships_left.show_text()

    def rounder(self, value):
        # Round the score and make it easy to read
        rounded_no = round(value, -1)
        string = "{:,}".format(rounded_no)
        return string


class ScreenText:
    """A class manage characteristics of scoring information."""
    def __init__(self, bg_color, side_of_screen, position_x, position_y, screen):
        self.screen = screen
        self.bg_color = bg_color
        self.image = None
        self.rect = None
        self.side_of_screen = side_of_screen
        self.pos_x = position_x
        self.pos_y = position_y
        self.text_color = (22, 146, 149)
        self.font = pygame.font.SysFont(None, 48)

    def update_values(self, newvalue):
        self.image = self.font.render(newvalue, True,
                                            self.text_color, self.bg_color)
        self.get_rectangle()

    def get_rectangle(self):
        # Display the score at the top right of the screen.
        self.rect = self.image.get_rect()
        if self.side_of_screen == "left":
            self.rect.left = self.pos_x
        elif self.side_of_screen == "right":
            self.rect.right = self.pos_x
        else:
            self.rect.center = self.pos_x

        self.rect.top = self.pos_y

    def show_text(self):
        self.screen.blit(self.image, self.rect)
