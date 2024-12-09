import pygame

class Background:
    def __init__(self):
        self.color = "beige"
    
    def draw(self, screen):
        screen.fill(self.color)

    def collide(self, player):
        SCREEN_HEIGHT = pygame.display.get_surface().get_height()
        if player.position[1] >= SCREEN_HEIGHT:
            return True
    
    def dead(self):
        self.color = "red"
        self.font = pygame.font.Font('additions/Tiny5-Regular.ttf', 400)
        self.text = self.font.render("Game Over", True, (0, 0, 0))
        self.textRect = self.text.get_rect()

    def winner(self):
        self.color = "green"
        self.font = pygame.font.Font('additions/Tiny5-Regular.ttf', 400)
        self.text = self.font.render("You Win", True, (0, 0, 0))
        self.textRect = self.text.get_rect()