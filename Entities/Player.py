import pygame

scavenge_tick = 0.5

class Player:

    def __init__(self):
        # Setting player attributes
        self.inventory = {
            "Wood Planks": 0,
            "Cement": 0,
            "Rope": 0,
            "Nails": 0,
            "Metal Scrap": 0,
            "Electronics": 0,
            "Fabric Scrap": 0,
            "Spare Parts": 0,
            "Gasoline": 0,
            "People": 0,
            "Batteries": 0
        }
    
        self.scavenging = False

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
        print( self.inventory)
        for item, quantity in self.inventory.items():
            print(f"  {item}: {quantity}")