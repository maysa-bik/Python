import pygame
from parametres import *
from grille import Grille

class Jeu:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()

    def nouveau(self):
        self.grille = Grille()
        self.grille.display_board()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else:
            self.end_screen()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.grille.draw(self.screen)
        pygame.display.flip()

    def check_win(self):
        for row in self.grille.board_list:
            for case in row:
                if case.type != "X" and not case.revealed:
                    return False
        return True

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:
                    if not self.grille.board_list[mx][my].flagged:
                        if not self.grille.dig(mx, my):
                            for row in self.grille.board_list:
                                for case in row:
                                    if case.flagged and case.type != "X":
                                        case.flagged = False
                                        case.revealed = True
                                        case.image = tile_not_mine
                                    elif case.type == "X":
                                        case.revealed = True
                            self.playing = False

                if event.button == 3:
                    if not self.grille.board_list[mx][my].revealed:
                        self.grille.board_list[mx][my].flagged = not self.grille.board_list[mx][my].flagged

                if self.check_win():
                    self.playing = False
                    for row in self.grille.board_list:
                        for case in row:
                            if not case.revealed:
                                case.flagged = True

    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
