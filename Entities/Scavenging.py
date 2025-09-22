import pygame
import random
import time 

# From Entities
from Entities.Player import scavenge_tick 

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
            "Gasoline": 1,    
            "People": 10,         
            "Batteries": 20,         
            "Electronics": 30,   
            "Spare Parts": 40,
            "Nails": 50,         
            "Metal Scrap": 60,    
            "Rope": 70,   
            "Fabric Scrap": 80,   
            "Cement": 90,     
            "Wood Planks": 100      
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
        if self.is_scavenging and current_time - self.scavenge_time >= scavenge_tick:
            self.scavenge_time = current_time
            rand = random.uniform(1, 100) 
            # Scavenging loop logic
            for item, chance in self.items.items():
                # Creates ranges for each items
                if rand <= chance:
                    # Adds to inventory
                    self.player.add_inventory(item, 1)
                    # Temp debugging line
                    print(f"Found 1 {item}")
                    # Resets loop to start
                    break
