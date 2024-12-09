import pygame

class Rect:
    all = []
    def __init__(self, x, y):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.position = (x*(SCREEN_WIDTH/30)+(SCREEN_WIDTH/6), y*(SCREEN_WIDTH/30)+(SCREEN_HEIGHT/15))
        self.color = "grey"

    def make(self):
        SCREEN_WIDTH = pygame.display.Info().current_w
        self.rect = pygame.Rect(self.position[0], self.position[1], 0.9*(SCREEN_WIDTH/30), 0.9*(SCREEN_WIDTH/30))
        Rect.all.append(self.rect)

    def collide(self, player):
        if self.rect.colliderect(player.rect):
            return True
        player.dx = -player.dx
        player.dy = -player.dy

    @classmethod
    def all_grids(cls):
        return Rect.all

class Grid:
    def __init__(self):
        for i in range(20):
            for j in range(10):
                Rect(i, j).make()