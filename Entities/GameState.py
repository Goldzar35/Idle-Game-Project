import pygame
from Entities.Scavenging import Scavenging
from Entities.Player import Player

# Game state would save a reference of the plater, current states of the menuus to make saves.

class GameState:
    def __init__(self):
        self.player = Player()
        # Track current menu
        self.current_menu = 0
        self.scavenging = Scavenging(self.player)

    def update_scavenging(self):
        # Check if scavenging is toggled on and update it
        if self.scavenging.is_scavenging:
            self.scavenging.scavenging()

