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
            self.background.draw(self.screen)
            self.bar.draw(self.screen)
            self.ball.draw(self.screen)
            self.ball.collide(self.bar)
            for i in Rect.all_grids():
                if i is not None and i.colliderect(self.ball.rect):
                    # Determine collision side
                    if self.ball.rect.bottom >= i.top and self.ball.rect.top < i.top:
                        self.ball.dy = -self.ball.dy  # Change vertical 
                    elif self.ball.rect.top <= i.bottom and self.ball.rect.bottom > i.bottom:
                        self.ball.dy = -self.ball.dy  # Change vertical direction
                    elif self.ball.rect.right >= i.left and self.ball.rect.left < i.left:
                        self.ball.dx = -self.ball.dx  # Change horizontal direction
                    elif self.ball.rect.left <= i.right and self.ball.rect.right > i.right:
                        self.ball.dx = -self.ball.dx  # Change horizontal direction
                    index = Rect.all_grids().index(i)
                    Rect.all_grids()[index] = None
                    break
                    
            for i in Rect.all_grids():
                if i is not None:
                    pygame.draw.rect(self.screen, "grey", i)
            if len(Rect.all_grids()) == 0 and not self.loose:
                self.won = True
            if self.won:
                SCREEN_WIDTH = pygame.display.get_surface().get_width()
                SCREEN_HEIGHT = pygame.display.get_surface().get_height()
                self.background.winner()
                self.screen.blit(self.background.text, (SCREEN_WIDTH/2-self.background.textRect.width/2, SCREEN_HEIGHT/2-self.background.textRect.height/2))
                self.bar.color = "beige"
            if self.background.collide(self.ball) and not self.won:
                self.loose = True
                SCREEN_WIDTH = pygame.display.get_surface().get_width()
                SCREEN_HEIGHT = pygame.display.get_surface().get_height()
                for i in Rect.all_grids():
                    Rect.all_grids().remove(i)
                self.background.dead()
                self.screen.blit(self.background.text, (SCREEN_WIDTH/2-self.background.textRect.width/2, SCREEN_HEIGHT/2-self.background.textRect.height/2))
                self.bar.color = "beige"
            self.ball.move()
            self.clock.tick(165)
            pygame.display.flip()
        pygame.quit()