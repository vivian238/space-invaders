# Space Invaders (Classic Arcade Game Written in Python Using PyGame Module)
# Code Written by Vivian

# _________Import PyGame, Random, & Sys Libraries_________
import pygame, sys
from pygame.locals import *
from random import shuffle

# _________Define Some Colors_________
#           R      G      B
BLACK  = (  0,     0,     0)
WHITE  = (255,   255,   255)
GREEN  = (  0,   255,     0)
YELLOW = (255,   255,     0)
RED    = (255,     0,     0)
PINK   = (250,   100,   250)
PURPLE = (160,     0,   250)
CYAN   = (  0,   255,   255)

# _________Create New Window_________
size = (650, 500)
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")

# _________Set Display, Player, Bullet, & Enemy Constants_________
GAME_TITLE = 'Space Invaders'                           # Display
BACKGROUND_COLOR = BLACK

PLAYER_ONE = 'Player 1'                                 # Player

BULLET_WIDTH = 5                                        # Bullet
BULLET_HEIGHT = 5

ENEMY_WIDTH = 25                                        # Enemy
ENEMY_HEIGHT = 25
ENEMY = 'Enemy'
