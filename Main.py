import pygame
from DefaultMenu import *
from InventoryMenu import *
from ShopMenu import *
from ScavengingMenu import *
from ForagingMenu import *
from HuntingMenu import *
from EngineeringMenu import *
from MedicineMenu import *
from CookingMenu import *
from FortificationMenu import *
from CommunityMenu import *
from LegacyMenu import *

pygame.init()
screen = pygame.display.set_mode((1100, 800)) # Screen size
screen.fill((40, 40, 40)) # Dark gray for the background color

#Sidebar size and demension
sidebar_width = 200
sidebar_height = 800
button_count = 12
button_height = 80
gap = 10

#Calculate total height and max scroll
total_height = button_count * button_height + (button_count + 1) * gap
max_scroll = max(0, total_height - sidebar_height)
scroll_offset = 0
scroll_speed = 10  # Adjust scroll speed as needed

#Defualt menu state
current_menu = 0 #0 for menu 1, 1 for menu 2...

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            scroll_offset -= event.y * scroll_speed
            scroll_offset = max(0, min(scroll_offset, max_scroll))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # 1 means left click
            mouse_x, mouse_y = event.pos #This has to be declared in this function does not work outside
            for i in range(button_count):
                y = gap + i * (button_height + gap) - scroll_offset
                if 0 <= mouse_x <= sidebar_width and y <= mouse_y <= y + button_height:
                    current_menu = i
#so all this above makes it so it can detect where the mouse is, because i is the event.pos which is the mouse position

    #Menus
    if current_menu == 0:
        draw_default_menu(screen) #Default Menu
    elif current_menu == 1:
        draw_inventory_menu(screen) #Inventory Menu
    elif current_menu == 2:
        draw_shop_menu(screen) #Shop Menu
    elif current_menu == 3:
        draw_scavenging_menu(screen) #Scavenging Menu
    elif current_menu == 4:
        draw_foraging_menu(screen) #Foraging Menu
    elif current_menu == 5: 
        draw_hunting_menu(screen) #Hunting Menu
    elif current_menu == 6:
        draw_engineering_menu(screen) #Engineering Menu
    elif current_menu == 7:
        draw_medicine_menu(screen) #Medicine Menu
    elif current_menu == 8:
        draw_cooking_menu(screen) #Cooking Menu
    elif current_menu == 9:
        draw_fortification_menu(screen) #Fortification Menu
    elif current_menu == 10:
        draw_community_menu(screen) #Community Menu
    elif current_menu == 11:
        draw_legacy_menu(screen) #Legacy Menu

    pygame.draw.rect(screen, (30, 30, 30), (0, 0, 200, 800)) # First 3 values are color, other 4 are x, y, width, height this is the sidebar

        # Draw buttons with scroll
    for i in range(button_count):
        y = gap + i * (button_height + gap) - scroll_offset
        if -button_height < y < sidebar_height:  # Only draw visible buttons
            pygame.draw.rect(screen, (50, 50, 50), (0, y, sidebar_width, button_height))
    
    pygame.display.flip() #Updates the display

pygame.quit()
