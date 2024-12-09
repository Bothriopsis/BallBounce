import pygame

class movingBar:
    def __init__(self):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.position = [(SCREEN_WIDTH/2-SCREEN_WIDTH/16), (9*(SCREEN_HEIGHT/10))]
        self.color = "darkblue"

    def draw(self, screen):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.rect = pygame.Rect(self.position[0], self.position[1], SCREEN_WIDTH/8, SCREEN_HEIGHT/100)
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, x):
        self.position[0] += x