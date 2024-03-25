# menu.py
import pygame
from parametres import *

class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menu")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.screen.fill(BGCOLOUR)
            self.draw_menu()
            pygame.display.flip()

    def draw_menu(self):
        title_text = self.font.render("Menu Principal", True, White)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        easy_text = self.font.render("Facile", True, White)
        easy_rect = easy_text.get_rect(center=(WIDTH // 2, 200))
        self.screen.blit(easy_text, easy_rect)

        medium_text = self.font.render("Moyen", True, White)
        medium_rect = medium_text.get_rect(center=(WIDTH // 2, 300))
        self.screen.blit(medium_text, medium_rect)

        hard_text = self.font.render("Difficile", True, White)
        hard_rect = hard_text.get_rect(center=(WIDTH // 2, 400))
        self.screen.blit(hard_text, hard_rect)

        mouse_pos = pygame.mouse.get_pos()

        if easy_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Yellow, easy_rect, 3)
            if pygame.mouse.get_pressed()[0]:
                return "facile"
        if medium_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Yellow, medium_rect, 3)
            if pygame.mouse.get_pressed()[0]:
                return "moyen"
        if hard_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, Yellow, hard_rect, 3)
            if pygame.mouse.get_pressed()[0]:
                return "difficile"
