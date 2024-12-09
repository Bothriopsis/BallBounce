import pygame

class Background:
    def __init__(self):
        self.color = "teal"
    
    def draw(self, screen):
        screen.fill(self.color)
    
    def dead(self):
        self.color = "red"
        self.font = pygame.font.Font('additions/Tiny5-Regular.ttf', 74)
        self.text = self.font.render("Game Over", True, (0, 0, 0))