import pygame

class Background:
    def __init__(self):
        self.color = "black"
    
    def draw(self, screen):
        screen.fill(self.color)