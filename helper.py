import pygame
def draw_button(screen, rect, color, text, font):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (rect.x + 10, rect.y + 10))

def is_clicked(rect, event):
    return event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos)
