import random
import pygame

class bounciBall:
    def __init__(self):
        SCREEN_WIDTH = pygame.display.Info().current_w
        SCREEN_HEIGHT = pygame.display.Info().current_h
        self.position = [random.randint(int(SCREEN_WIDTH/50),int(49*SCREEN_WIDTH/50)),random.randint(int(SCREEN_HEIGHT*5/6),int(SCREEN_HEIGHT-SCREEN_WIDTH/50))]
        self.color = "purple"
        self.dx = random.randint(50,100)/50 # Random velocity on x-Achsis
        self.dy = random.randint(-100,-50)/50 # Rnadom velocitiy on y-Achsis in positiv Direction towards the grid

    def draw(self, screen):
        SCREEN_WIDTH = pygame.display.Info().current_w
        self.rect = pygame.Rect(self.position[0], self.position[1], SCREEN_WIDTH/50, SCREEN_WIDTH/50)
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self):
        self.position[0] += self.dx
        self.position[1] += self.dy

    def collide(self, bar):
        SCREEN_WIDTH = pygame.display.Info().current_w
        if self.position[0] <= 0 or self.position[0] >= SCREEN_WIDTH - SCREEN_WIDTH/50:
            self.dx = -self.dx
        if self.position[1] <= 0:
            self.dy = -self.dy
        if self.rect.colliderect(bar.rect):
            self.dy = -self.dy
        


