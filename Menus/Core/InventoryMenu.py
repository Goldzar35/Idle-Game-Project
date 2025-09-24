import pygame

# From Entities
from Entities.Player import * 

class InventoryMenu:
    def __init__(self, player, sidebar_width):
        # Store reference to player
        self.player = player
        self.sidebar_width = sidebar_width
        self.margin = 30

    def update_dimensions(self, sidebar_width, window_height):
        if sidebar_width != self.sidebar_width:
            self.sidebar_width = sidebar_width
        self.margin = int(0.03 * window_height)

    def draw(self, screen):
        screen.fill((50, 50, 50)) 
        font = pygame.font.Font(None, 36)
        y = self.margin

        # Temp inventory display logic
        for item, quantity in self.player.inventory.items():
            text = f"{item}: {quantity}"
            text_surf = font.render(text, True, (255, 255, 255))
            screen.blit(text_surf, (self.sidebar_width + 20, y))
            y += 40

    def add_inventory(self, item, quantity):
        self.player.add_inventory(item, quantity)

    def remove_inventory(self, item, quantity):
        self.player.remove_from_inventory(item, quantity)