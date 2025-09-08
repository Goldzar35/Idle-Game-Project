import pygame

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            scroll_offset -= event.y * scroll_speed
            scroll_offset = max(0, min(scroll_offset, max_scroll))

    screen.fill((40, 40, 40)) # Dark gray for the background color

    pygame.draw.rect(screen, (30, 30, 30), (0, 0, 200, 800)) # First 3 values are color, other 4 are x, y, width, height this is the sidebar

        # Draw buttons with scroll
    for i in range(button_count):
        y = gap + i * (button_height + gap) - scroll_offset
        if -button_height < y < sidebar_height:  # Only draw visible buttons
            pygame.draw.rect(screen, (50, 50, 50), (0, y, sidebar_width, button_height))

    pygame.display.flip() #Updates the display

pygame.quit()
