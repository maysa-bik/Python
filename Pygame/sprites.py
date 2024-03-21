import pygame
from settings import *

# types list
# "." -> unknown (غير معروف)
# "x" -> mine ( boombe / لغم)
# "c" -> clue ( index)
# "/" -> empty (vide /  فارغ)

class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.image = image 
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def draw(self, board_surface):
        board_surface.blit(tile_unknown, (self.x, self.y))



    def __repr__(self): # تعني  من اجل التكرار الصفوف لكي يرسم لنا شبكه 
        return self.type

class Board:
    def __init__(self):
       # dans le page settings (WIDTH = TileSize * Rows / HEIGHT = TileSize * Cols)
       self.board_surface = pygame.Surface((WIDTH, HEIGHT)) 
       """
       pour eviter le repiter 
       par exemple pour pas dessiner le grille comm 
       self.board_list = [
            [tile, tile, tile, tile],
            [tile, tile, tile, tile],
            [tile, tile, tile, tile],
            [tile, tile, tile, tile],
       ]
       موضع النقطه كنوع لقائمة مقبولة في قائمة اللوحات 
       tile_empty مربع فارغ كصورة 
       """
       self.board_list = [[Tile(col, row, tile_empty, ".") for row in range(ROWS)] for col in range(COLS)] 
    
    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, (0, 0))        

    def display_board(self):
        for row in self.board_list:
            print(row)

            
