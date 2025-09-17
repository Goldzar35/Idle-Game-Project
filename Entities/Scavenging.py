import pygame
import random
import time 

# From Entities
from Entities.Player import Player

class Scavenging:
    def __init__(self, player):
        # Initialize player
        self.player = player
        # References Scavenging not the player
        self.is_scavenging = False
        # Scavenging per second
        self.scavenge_time = 0
        # Items list with probabilities
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
        # Time check between scavenging actions
        current_time = time.time()
        # RNG element
        if self.is_scavenging and current_time - self.scavenge_time >= 0.5:
            self.scavenge_time = current_time
            rand = random.uniform(0, 1) 
            # Compares random nummber to probabilitties of items
            cumulative_probability = 0

            # Scavenging loop logic
            for item, chance in self.items.items():
                # Creates ranges for each items
                cumulative_probability += chance
                if rand < cumulative_probability:
                    # Adds to inventory
                    self.player.add_inventory(item, 1)
                    # Temp debugging line
                    print(f"Found 1 {item}")
                    # Ressets loop to start
                    break
