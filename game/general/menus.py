import pygame

class MainMenu:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.play_button = Button(ai_game, "Play")

    def show_menu(self, game_active):
        if not game_active:
            # Draw the play button if the game is inactive.
            self.play_button.draw_button()

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.ai_game.stats.game_active = True
            pygame.mouse.set_visible(False)


class RetryMenu:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.play_button = Button(ai_game, "Play")
        self.screen_rect = ai_game.screen.get_rect()

        # Game over text heads up
        self.text_color = (88, 0, 0)
        self.game_over = pygame.font.SysFont(None, 100)
        self.g_o_rect = None
        self.g_o_str = "GAME OVER"
        self.g_o_image = self.game_over.render(self.g_o_str, True,
                                                  self.text_color, self.ai_game.settings.bg_color)

        self.g_o_rect = self.g_o_image.get_rect()
        self.g_o_rect.center = self.screen_rect.center
        self.g_o_rect.top = 300

    def show_menu(self, game_active):
        if not game_active:
            # Draw the play button if the game is inactive.
            self.ai_game.screen.blit(self.g_o_image, self.g_o_rect)
            self.play_button.draw_button()
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.ai_game.stats.reset_stats()
            self.ai_game.stats.game_active = True
            self.ai_game.sb.prep_score()


class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (88, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
