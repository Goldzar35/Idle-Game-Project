import pygame
from Entities.Player import Player
from Entities.Scavenging import *

class ScavengingMenu:
    def __init__(self, player):
        # Initialize anything specific to the Scavenging Menu here
        self.margin = 30
        self.sidebar_width = 200
        self.player = player
        self.scavenging = Scavenging(player)  # Create an instance of Scavenging

    # Scavenging box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = 1100 - self.sidebar_width - 2 * self.margin
        self.box_height = 800 / 2 - 2 * self.margin

    # create a rectangle for the scavenging box
        self.scavenge_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

    def draw(self, screen):
        screen.fill((70, 70, 70)) # Background color for the scavenging menu
        pygame.draw.rect(screen, (100, 100, 100), self.scavenge_box)  # Draw the scavenging box

    def handle_scavenge_event(self, event,):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_x, mouse_y = event.pos
            if self.scavenge_box.collidepoint(mouse_x, mouse_y):
                self.scavenging.toggle_scavenging()





        