import sys
import pygame

# import the game
from game.alrimal_game import AlrimalGame

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlrimalGame()
    ai.run_game()
