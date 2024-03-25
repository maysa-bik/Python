import pygame
from parametres import *
from grille import Grille

class Jeu:
    def __init__(self):
        # Initialisation de la fenêtre du jeu
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper")  # Titre de la fenêtre
        self.clock = pygame.time.Clock()  # Horloge pour contrôler le framerate

    def nouveau(self):
        # Création d'une nouvelle grille de jeu
        self.grille = Grille()
        self.grille.afficher_grille()  # Affichage de la grille
        self.temps_debut = pygame.time.get_ticks() // 1000  # Temps en secondes
        self.score = 0  # Initialisation du score
        self.mines_restantes = AMOUNT_MINES  # Initialisation du nombre de mines restantes

        # Initialisation de la police de caractères pour l'affichage du temps
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def run(self):
        self.playing = True
        self.nouveau()  # Début d'une nouvelle partie
        while self.playing:
            self.clock.tick(FPS)  # Contrôle du framerate
            temps_actuel = pygame.time.get_ticks() // 1000  # Temps actuel en secondes
            temps_passe = temps_actuel - self.temps_debut  # Calcul du temps écoulé
            self.events()  # Gestion des événements
            self.dessiner(temps_passe)  # Dessin de la grille et du temps écoulé
        else:
            self.fin_ecran()  # Fin de la partie

    def dessiner(self, temps_passe):
        self.screen.fill(BGCOLOUR)  # Remplissage de l'écran avec la couleur de fond
        self.grille.dessiner(self.screen)  # Dessin de la grille
        # Affichage du temps écoulé à l'écran
        temps_texte = self.font.render("Temps: " + str(temps_passe), True, Black)
        self.screen.blit(temps_texte, (10, 10))  # Affichage du temps en haut à gauche
        pygame.display.flip()  # Rafraîchissement de l'écran

    def check_gagn(self):
        # Vérification si toutes les cases sans mine ont été révélées
        for row in self.grille.grille_list:
            for case in row:
                if case.type != "X" and not case.revealed:
                    return False
        return True

    def events(self):
        # Gestion des événements (clics de souris, fermeture de fenêtre)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                mx //= TILESIZE
                my //= TILESIZE

                if event.button == 1:  # Clic gauche
                    if not self.grille.grille_list[mx][my].flagged:
                        # Si le joueur a creusé une mine
                        if not self.grille.creuser(mx, my):
                            for row in self.grille.grille_list:
                                for case in row:
                                    if case.flagged and case.type != "X":
                                        case.flagged = False
                                        case.revealed = True
                                        case.image = tile_not_mine
                                    elif case.type == "X":
                                        case.revealed = True
                            self.playing = False  # Fin de la partie en cas de défaite

                if event.button == 3:  # Clic droit
                    if not self.grille.grille_list[mx][my].revealed:
                        # Alternance entre drapeau, point d'interrogation et état inconnu
                        self.grille.grille_list[mx][my].flagged = not self.grille.grille_list[mx][my].flagged

                if self.check_gagn():
                    # Si le joueur a gagné
                    self.gagn = True
                    self.playing = False
                    for row in self.grille.grille_list:
                        for case in row:
                            if not case.revealed:
                                case.flagged = True  # Marquage des cases non révélées comme des mines

    def fin_ecran(self):
        # Écran de fin de partie
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return  # Retour au menu principal

# Initialisation de la classe Jeu et boucle principale du jeu
jeu = Jeu()
while True:
    jeu.nouveau()  # Lancement d'une nouvelle partie
    jeu.run()  # Exécution de la partie
              
