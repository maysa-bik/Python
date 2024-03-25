# Colors 
import os
import pygame


White = (255, 255, 255)
Black = (0, 0, 0)
DarkGrey = (40, 40, 40)
LightGrey = (100, 100, 100)
Green = (0, 255, 0)
DarkGreen = (0, 200, 0)
Blue = (0, 0, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
BGCOLOUR = DarkGrey

# game paramaitres :
TILESIZE = 32
ROWS = 15
COLS = 15
AMOUNT_MINES = 10
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60
TITLE = "MinesWeeper"

tile_numbers = []
for i in range(1, 9):
    #  pour changer le size de photo (pygame.transform.scale) avec le size de carée pour ça on mis (TILESIZE, TILESIZE)
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Photoes", f"Tile{i}.png")), (TILESIZE, TILESIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("Photoes", "TileEmpty.png")), (TILESIZE, TILESIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("Photoes", "TileExploded.png")), (TILESIZE, TILESIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("Photoes", "TileFlag.png")), (TILESIZE, TILESIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("Photoes", "TileMine.png")), (TILESIZE, TILESIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("Photoes", "TileUnknown.png")), (TILESIZE, TILESIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("Photoes", "TileNotMine.png")), (TILESIZE, TILESIZE))