import sys
import pygame

# Import the game
from game.alrimal_game import AlrimalGame

# Starts the game
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlrimalGame()
    ai.run_game()
