import pygame

pygame.init()
screen = pygame.display.set_mode((1100, 800)) # Screen size
screen.fill((40, 40, 40)) # Dark gray for the background color
pygame.display.set_caption("Idle Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 40, 40)) # Dark gray for the background color

    pygame.draw.rect(screen, (30, 30, 30), (0, 0, 200, 800)) # First 3 values are color, other 4 are x, y, width, height

    pygame.display.flip() #Updates the display

pygame.quit()
