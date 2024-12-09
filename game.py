import pygame
from gameObjects.moving import movingBar
from gameObjects.ball import bounciBall
from gameObjects.grid import Grid
from gameObjects.grid import Rect
from gameObjects.background import Background
import time

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
        self.won = False
        self.loose = False
        while self.game:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.game = False
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
            if len(Rect.all_grids()) == 0 and self.loose == False:
                self.won = True
            if self.won == True:
                SCREEN_WIDTH = pygame.display.get_surface().get_width()
                SCREEN_HEIGHT = pygame.display.get_surface().get_height()
                self.background.winner()
                self.screen.blit(self.background.text, (SCREEN_WIDTH/2-self.background.textRect.width/2, SCREEN_HEIGHT/2-self.background.textRect.height/2))
                self.bar.color = "beige"
            if self.background.collide(self.ball) and self.won == False:
                self.loose = True
                SCREEN_WIDTH = pygame.display.get_surface().get_width()
                SCREEN_HEIGHT = pygame.display.get_surface().get_height()
                for i in Rect.all_grids():
                    Rect.all_grids().remove(i)
                self.background.dead()
                self.screen.blit(self.background.text, (SCREEN_WIDTH/2-self.background.textRect.width/2, SCREEN_HEIGHT/2-self.background.textRect.height/2))
                self.bar.color = "beige"
            self.clock.tick(165)
            pygame.display.flip()
        pygame.quit()