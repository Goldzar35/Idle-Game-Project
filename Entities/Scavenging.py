import pygame
import random
import time 
from Entities.Player import Player

class Scavenging:
    def __init__(self, player):
        # Initialize player
        self.player = player
        # References Scavenging not the player
        self.is_scavenging = False
        # Scavenging per second
        self.scavenge_time = 0
        # Items list would go here
        self.items = {
            "wood": .5,
            "stone": .3,
            "food": .2
        }
    
    def toggle_scavenging(self):
        # Acts as a toggle switch
        self.is_scavenging = not self.is_scavenging
        # Check to see if it works
        print(f"Scavenging {'started' if self.is_scavenging else 'stopped'}")

    def scavenging(self):
        current_time = time.time()
        if self.is_scavenging and current_time - self.scavenge_time >= 0.5:
            self.scavenge_time = current_time
            rand = random.uniform(0, 1)  # Generate a random number between 0 and 1
            cumulative_probability = 0

            # Scavenging loop logic
            for item, chance in self.items.items():
                cumulative_probability += chance
                if rand < cumulative_probability:
                    self.player.add_inventory(item, 1)
                    print(f"Found 1 {item}")
                    break
