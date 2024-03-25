from parametres import *

class Case:
    #Initialise une instance de Case avec les coordonnées (x, y), l'image associée, le type de contenu, et les états révélés et flaggés.
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def dessine(self, grille_surface):
        #Dessine la case sur la surface de la grille en fonction de son état actuel.
        if not self.flagged and self.revealed:
            grille_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            grille_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            grille_surface.blit(tile_unknown, (self.x, self.y))

    def __repr__(self):
        #Représentation de l'objet Case sous forme de chaîne de caractères.
        return self.type
