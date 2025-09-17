import pygame

# From Entities
from Entities.Player import * 

class InventoryMenu:
    def __init__(self, player):
        # Store reference to player
        self.player = player

    def draw(self, screen):
        screen.fill((50, 50, 50)) 

        font = pygame.font.Font(None, 36)
        y = 20

        # Temp inventory display logic
        for item, quantity in self.player.inventory.items():
            text = f"{item}: {quantity}"
            text_surf = font.render(text, True, (255, 255, 255))
            screen.blit(text_surf, (220, y))
            y += 40
    
    def add_inventory(self, item, quantity):
        self.player.add_inventory(item, quantity)

    def remove_inventory(self, item, quantity):
        self.player.remove_from_inventory(item, quantity)