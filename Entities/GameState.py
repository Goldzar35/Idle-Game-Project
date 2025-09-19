import pygame
from Entities.Scavenging import Scavenging
from Entities.Player import Player

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

