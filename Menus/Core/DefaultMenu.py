import pygame

class DefaultMenu:
    def __init__(self, player):
        # Initialize anything specific to the Default Menu here
        self.player = player

    def draw(self, screen):
        screen.fill((40, 40, 40))  