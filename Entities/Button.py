import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, screen, font):
        pygame.draw.rect(screen, (150, 150, 150), self.rect)  # Button color
        text_surf = font.render(self.text, True, (0, 0, 0))  # Text color
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        # Detects mouse click
        return self.rect.collidepoint(mouse_pos)