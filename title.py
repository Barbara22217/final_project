import pygame
from helper import draw_button, is_clicked

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Comfy Cakes")

FONT_LARGE = pygame.font.SysFont(None, 72)
FONT_MEDIUM = pygame.font.SysFont(None, 40)

PINK = (255, 228, 225)
BUTTON_COLOR = (255, 182, 193)

def title_screen():
    screen.fill(PINK)
    title_text = FONT_LARGE.render("Comfy Cakes", True, (0, 0, 0))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))

    start_button = pygame.Rect(WIDTH // 2 - 100, 350, 200, 60)
    draw_button(screen, start_button, BUTTON_COLOR, "Start Game", FONT_MEDIUM)

    pygame.display.flip()
    return start_button

def game_screen():
    screen.fill(PINK)
    info_text = FONT_MEDIUM.render("Game screen! (Work in progress)", True, (0, 0, 0))
    screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

def main():
    running = True
    in_title = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if in_title and event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    in_title = False

        if in_title:
            start_button = title_screen()
        else:
            game_screen()

    pygame.quit()

if __name__ == "__main__":
    main()
