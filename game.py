import pygame
from gameObjects.moving import movingBar
from gameObjects.ball import bounciBall

class Game:
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bar = movingBar()
    ball = bounciBall()

