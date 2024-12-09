import pygame

class Background:
    def __init__(self):
        self.color = "teal"
    
    def draw(self, screen):
        screen.fill(self.color)

    def collide(self, player):
        SCREEN_HEIGHT = pygame.display.get_surface().get_height()
        if player.rect.y >= SCREEN_HEIGHT:
            return True
    
    def dead(self):
        self.color = "red"
        self.font = pygame.font.Font('additions/Tiny5-Regular.ttf', 74)
        self.text = self.font.render("Game Over", True, (0, 0, 0))