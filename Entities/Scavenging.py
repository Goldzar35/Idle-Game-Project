import pygame
from Entities.Player import Player

class Scavenging:
    def __init__(self, player):
        self.player = player
        # References Scavenging not the player
        self.is_scavenging = False
        # Items list would go here
    
    def toggle_scavenging(self):
        # Acts as a toggle switch
        self.is_scavenging = not self.is_scavenging
        # Check to see if it works
        print(f"Scavenging {'started' if self.is_scavenging else 'stopped'}")

    def scavenging(self):
        pass


