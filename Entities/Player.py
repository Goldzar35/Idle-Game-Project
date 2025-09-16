import pygame

class Player:
    def __init__(self):
        # Setting player attributes
        self.inventory = {
            "wood": 0,
            "stone": 0,
            "food": 0
        }
        
        self.scavenging = False

    # Scavenging logic
    def is_scavenging(self):
        return self.scavenging

    def set_scavenging(self, state):
        self.scavenging = state
        print("Scavenging state set to:", state)

    # Inventory logic
    def add_inventory(self, items, quantity):
        if items in self.inventory:
            self.inventory[items] += quantity
        else:
            self.inventory[items] = quantity

    def remove_inventory(self, item, quantity):
        if item in self.player.inventory and self.player.inventory[item] >= quantity:
            self.player.inventory[item] -= quantity
        else:
            pass

    def show_inventory(self):
        print("Player's inventory:", self.inventory)
        for item, quantity in self.inventory.items():
            print(f"  {item}: {quantity}")