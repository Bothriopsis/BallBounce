import pygame

class Rect:
    def __init__(self, x, y):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.x = x
        self.y = y
        self.position = (x*(SCREEN_WIDTH/30)+(SCREEN_WIDTH/6), y*(SCREEN_WIDTH/30)+(SCREEN_HEIGHT/15))
        self.color = "grey"

    def draw(self, screen):
        SCREEN_WIDTH = pygame.display.Info().current_w
        self.rect = pygame.Rect(self.position[0], self.position[1], 0.9*(SCREEN_WIDTH/30), 0.9*(SCREEN_WIDTH/30))
        pygame.draw.rect(screen, self.color, self.rect)
    
    def canCollide(self, other):
        if self.position[0] == other.position[0]:
            print("collided")
        if self.position[1] == other.position[1]:
            print("collided")

class Grid(Rect):
    def __init__(self, x, y):
        super().__init__(x, y)
        for i in range(20):
            for j in range(10):
                self.grid.append(Rect(i, j))
    
    def canCollide(self, other):
        return super().canCollide(other)