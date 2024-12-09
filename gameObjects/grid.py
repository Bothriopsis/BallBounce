import pygame

class Rect:
    def __init__(self, x, y):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.x = x
        self.y = y
        self.position = (x*(SCREEN_WIDTH/30)+(SCREEN_WIDTH/6), y*(SCREEN_WIDTH/30)+(SCREEN_HEIGHT/15))
        self.color = "grey"

    def make(self, screen, rect):
        SCREEN_WIDTH = pygame.display.Info().current_w
        rect = pygame.Rect(self.position[0], self.position[1], 0.9*(SCREEN_WIDTH/30), 0.9*(SCREEN_WIDTH/30))
        pygame.draw.rect(screen, self.color, rect)

class Grid(Rect):
    def __init__(self, screen):
        self.grid = []
        for i in range(20):
            for j in range(10):
                super().__init__(i,j)

    def exist(self, screen):
        for g in self.grid:
            pygame.draw.rect(screen, self.color, g)
            print(g)
            
    
    def canCollide(self, other):
        for i in self.grid:
            if i.position[0] == other.position[0]:
                self.grid.remove(i)
            if i.position[1] == other.position[1]:
                self.grid.remove(i)