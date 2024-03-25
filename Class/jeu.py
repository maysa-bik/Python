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
        self.grille.afficher_grille()
        self.temps_debut = pygame.time.get_ticks() // 1000  # Temps en secondes
        self.score = 0
        self.mines_restantes = AMOUNT_MINES

        # Initialisation de la police de caractères pour l'affichage du temps
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        

    def run(self):
        self.playing = True
        self.nouveau()
        while self.playing:
            self.clock.tick(FPS)
            temps_actuel = pygame.time.get_ticks() // 1000
            temps_passe = temps_actuel - self.temps_debut
            self.events()
            self.dessiner(temps_passe)
            #self.dessiner()
        else:
            self.fin_ecran()

    def dessiner(self, temps_passe):
        self.screen.fill(BGCOLOUR)
        self.grille.dessiner(self.screen)
        # Affichage du temps écoulé à l'écran
        temps_texte = self.font.render("Temps: " + str(temps_passe), True, Black)
        self.screen.blit(temps_texte, (10, 10))
        pygame.display.flip()

    def check_gagn(self):
        for row in self.grille.grille_list:
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

                if event.button == 1: # click gauch
                    if not self.grille.grille_list[mx][my].flagged:
                        if not self.grille.creuser(mx, my):
                            for row in self.grille.grille_list:
                                for case in row:
                                    if case.flagged and case.type != "X":
                                        case.flagged = False
                                        case.revealed = True
                                        case.image = tile_not_mine
                                    elif case.type == "X":
                                        case.revealed = True
                            self.playing = False

                if event.button == 3:  # Clic droit
                    if not self.grille.grille_list[mx][my].revealed:
                        self.grille.grille_list[mx][my].flagged = not self.grille.grille_list[mx][my].flagged

                if self.check_gagn():
                    self.gagn = True
                    self.playing = False
                    for row in self.grille.grille_list:
                        for case in row:
                            if not case.revealed:
                                case.flagged = True


    def fin_ecran(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return
jeu = Jeu()
while True:
    jeu.nouveau()
    jeu.run()                
