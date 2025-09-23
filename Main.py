import pygame

# From Entities
from Entities.Player import Player
from Entities.Button import Button
from Entities.GameState import GameState

# From Menus
from Menus.Core.DefaultMenu import DefaultMenu
from Menus.Core.InventoryMenu import InventoryMenu
from Menus.Core.ShopMenu import ShopMenu
from Menus.Skills.ScavengingMenu import *
from Menus.Skills.ForagingMenu import ForagingMenu
from Menus.Skills.HuntingMenu import HuntingMenu
from Menus.Skills.EngineeringMenu import EngineeringMenu
from Menus.Skills.MedicineMenu import MedicineMenu
from Menus.Skills.CookingMenu import CookingMenu
from Menus.Skills.FortificationMenu import FortificationMenu
from Menus.Skills.CommunityMenu import CommunityMenu
from Menus.Skills.LegacyMenu import LegacyMenu

# Initialize player
player = Player()

# Initialize pygame
pygame.init()

# Initialize GameState
game_state = GameState()

# Initial window size
info = pygame.display.Info()
window_width, window_height = info.current_w, info.current_h

# Minimum window size
MIN_WIDTH = 800
MIN_HEIGHT = 800

# Base Display
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
screen.fill((40, 40, 40))

# Sidebar size and demension variables
sidebar_width = int(0.2 * window_width)
sidebar_height = window_height
button_count = 12
button_height = int(0.1 * window_height)
gap = int(0.01 * window_height)
font = pygame.font.SysFont(None, 36)

# Button names
sidebar_buttons = []
button_names = ["Default", "Inventory", "Shop", "Scavenging", "Foraging", "Hunting", "Engineering", "Medicine", "Cooking", "Fortification", "Community", "Legacy"]

# Calculate total height and max scroll
total_height = button_count * button_height + (button_count + 1) * gap
max_scroll = max(0, total_height - sidebar_height)
scroll_offset = 0
scroll_speed = 15 

# Draw the sidebar background
pygame.draw.rect(screen, (30, 30, 30), (0, 0, 200, 800)) 

# Initalize buttons
for i, name in enumerate(button_names):
    y = gap + i * (button_height + gap)
    # 0 is the x value, y value, sidebar_width, button_height, name, i determines button index
    btn = Button(0, y, sidebar_width, button_height, name, i) 
    # append adds a new button to the list
    sidebar_buttons.append(btn)


# Add other Menu's here
menus = {
    0: DefaultMenu(game_state.player),
    1: InventoryMenu(game_state.player, sidebar_width),
    2: ShopMenu(game_state.player),
    3: ScavengingMenu(game_state.player, game_state, sidebar_width, window_width, window_height),
    4: ForagingMenu(game_state.player),
    5: HuntingMenu(game_state.player),
    6: EngineeringMenu(game_state.player),
    7: MedicineMenu(game_state.player),
    8: CookingMenu(game_state.player),
    9: FortificationMenu(game_state.player),
    10: CommunityMenu(game_state.player),
    11: LegacyMenu(game_state.player)
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Ensure minimum size
            new_width = max(event.w, MIN_WIDTH)
            new_height = max(event.h, MIN_HEIGHT)
            # Update Screen Size
            screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
            window_width, window_height = new_width, new_height
            # Sidebar and button dimensions
            sidebar_width = int(0.2 * window_width)
            sidebar_height = window_height
            button_height = int(0.1 * window_height)
            gap = int(0.01 * window_height)
            # Recalculate height and max scroll
            total_height = button_count * button_height + (button_count + 1) * gap
            max_scroll = max(0, total_height - sidebar_height)
            # Update button rects
            for i, btn in enumerate(sidebar_buttons):
                y = gap + i * (button_height + gap)
                btn.rect = pygame.Rect(0, y, sidebar_width, button_height)
        if game_state.current_menu == 3:
            menus[3].update_dimensions(window_width, window_height)
        if  game_state.current_menu == 1:
            menus[1].update_dimensions(sidebar_width, window_height)
        elif event.type == pygame.MOUSEWHEEL:
            scroll_offset -= event.y * scroll_speed
            scroll_offset = max(0, min(scroll_offset, max_scroll)) 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            mouse_x, mouse_y = event.pos
            # Handle sidebar button clicks
            for btn in sidebar_buttons:
                if btn.is_clicked((mouse_x, mouse_y)):
                    # Switch to selected menu
                    game_state.current_menu = btn.action  
        # For Scavenging
        if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "handle_scavenge_event"):
            menus[game_state.current_menu].handle_scavenge_event(event)

    # Update scavenging logic globally
    game_state.update_scavenging()
    
    # Draw the current menu background
    if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "draw"):
        menus[game_state.current_menu].draw(screen)

    # Update buttons
    for i, btn in enumerate(sidebar_buttons):
        # Adjust button position for scrolling
        btn.rect.y = gap + i * (button_height + gap) - scroll_offset
        # Only draw buttons that are visible in the sidebar
        if -button_height < btn.rect.y < sidebar_height:
            btn.draw(screen, font)

    # Updates display
    pygame.display.flip() 

pygame.quit()

