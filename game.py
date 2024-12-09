import pygame
from gameObjects.moving import movingBar
from gameObjects.ball import bounciBall
from gameObjects.grid import Grid
from gameObjects.background import Background

class Game:
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    bar = movingBar()
    ball = bounciBall()
    grid = Grid(screen)
    background = Background()
    def __init__(self):
        self.game = True
    
    def run(self):
        while self.game:
            if not self.background.collide(self.ball):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.bar.move(-10)
                if keys[pygame.K_RIGHT]:
                    self.bar.move(10)
                self.ball.move()
                self.background.draw(self.screen)
                self.bar.draw(self.screen)
                self.ball.draw(self.screen)
                self.ball.collide(self.bar)
                self.grid.exist(self.screen)
                pygame.display.flip()
                self.clock.tick(1)
            
        pygame.quit()