import random
import pygame
from parametres import *
from case import Case

class Grille:
    def __init__(self):
        # Initialisation de la surface de la grille
        # dans le page settings (WIDTH = TileSize * Rows / HEIGHT = TileSize * Cols)
        self.grille_surface = pygame.Surface((ROWS * TILESIZE, COLS * TILESIZE))
        """
       pour eviter le repiter 
       par exemple pour pas dessiner le grille comm 
       self.grille_list = [
            [tile, tile, tile, tile],
            [tile, tile, tile, tile],
            [tile, tile, tile, tile],
            [tile, tile, tile, tile],
       ]
       موضع النقطه كنوع لقائمة مقبولة في قائمة اللوحات 
       tile_empty مربع فارغ كصورة 
       """
        # Création de la grille avec des cases initialisées à vide
        self.grille_list = [[Case(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)]
        # Placement des mines et des indices
        self.place_mines()
        self.place_indices()
        # Liste pour suivre les cases creusées
        self.dug = [] # متغير سيكون قائمة فارغة سنقوم بتخزين جميع قيم التي حفرها بالفعل 

    def place_mines(self):
        # Placement aléatoire des mines sur la grille
        for _ in range(AMOUNT_MINES):
            while True:
                x = random.randint(0, ROWS - 1)
                y = random.randint(0, COLS - 1)

                if self.grille_list[x][y].type == ".":
                    self.grille_list[x][y].image = tile_exploded
                    self.grille_list[x][y].type = "X"
                    break

    def place_indices(self):
        # Placement des indices indiquant le nombre de mines adjacentes à chaque case
        for x in range(ROWS):
            for y in range(COLS):
                if self.grille_list[x][y].type != "X":
                    total_mines = self.verifier_voisins(x, y)
                    if total_mines > 0:
                        self.grille_list[x][y].image = tile_numbers[total_mines - 1]
                        self.grille_list[x][y].type = "C"

    @staticmethod # طريقة ثابتة 
    def interieur(x, y):
        # Vérifie si les coordonnées (x, y) sont à l'intérieur de la grille
        return 0 <= x < ROWS and 0 <= y < COLS # اذا كان اقل او يساوي عدد الصفوف / الاعمدة 

    #نستدعي هذه الطريقة لنعرف المربع المجاور الذ نتحقق منه موجودا بالفعل داخل اللوحات لانه اذا لم يكم الاكر كذلك فلا يمكننا 
  
    def verifier_voisins(self, x, y):
        # Vérifie le nombre de mines dans les cases voisines
        total_mines = 0
        for x_offset in range(-1, 2):
            for y_offset in range(-1, 2):
                voisin_x = x + x_offset
                voisin_y = y + y_offset
                # اريد ان اتاكد من ان الجار x والجار y  موجودان داخل اللوحات واذا لم يكن كذلك لم يكن لديك هذا التحقق فسيتم تكراره وستعطيه خطأ  نريج التحقق ممل اذا كانت هذه الاحذاثيات بالداخل 
                # نحن منحقق ايضا مما اذا كان هذا الجار منجما 
                if self.interieur(voisin_x, voisin_y) and self.grille_list[voisin_x][voisin_y].type == "X":
                    total_mines += 1
        return total_mines

    def dessiner(self, screen):
        # Dessine la grille à l'écran
        for row in self.grille_list:
            for case in row:
                case.dessine(self.grille_surface)
        screen.blit(self.grille_surface, (0, 0))

    def creuser(self, x, y):
        # Permet de creuser une case et de révéler son contenu
        self.dug.append((x, y))
        if self.grille_list[x][y].type == "X":
            self.grille_list[x][y].revealed = True
            self.grille_list[x][y].image = tile_exploded
            return False
        elif self.grille_list[x][y].type == "C":
            self.grille_list[x][y].revealed = True
            return True

        self.grille_list[x][y].revealed = True

        for row in range(max(0, x - 1), min(ROWS - 1, x + 1) + 1):
            for col in range(max(0, y - 1), min(COLS - 1, y + 1) + 1):
                if (row, col) not in self.dug:
                    self.creuser(row, col)
        return True

    def afficher_grille(self):
        # Affiche la grille dans la console
        for row in self.grille_list:
            print(row)
