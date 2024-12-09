import pygame
from gameObjects.moving import movingBar
from gameObjects.ball import bounciBall
from gameObjects.grid import Grid
from gameObjects.grid import Rect
from gameObjects.background import Background

class Game:
    pygame.init()
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bar = movingBar()
    ball = bounciBall()
    grid = Grid()
    background = Background()
    def __init__(self):
        self.game = True

    def run(self):
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.bar.move(-10)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.bar.move(10)
            self.ball.move()
            self.background.draw(self.screen)
            self.bar.draw(self.screen)
            self.ball.draw(self.screen)
            self.ball.collide(self.bar)
            for i in Rect.all_grids():
                if i.colliderect(self.ball.rect):
                    Rect.all_grids().remove(i)
                pygame.draw.rect(self.screen, "grey", i)
            if self.background.collide(self.ball):
                self.background.dead()
            self.clock.tick(165)
            pygame.display.flip()
        pygame.quit()