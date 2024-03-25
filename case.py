from parametres import *

class Case:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def dessine(self, grille_surface):
        if not self.flagged and self.revealed:
            grille_surface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            grille_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            grille_surface.blit(tile_unknown, (self.x, self.y))

    def __repr__(self):
        return self.type
