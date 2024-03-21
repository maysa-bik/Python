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
TileSize = 32
Rows = 15
Cols = 15
Amount_Mines = 5
WIDTH = TileSize * Rows
HEIGHT = TileSize * Cols
FPS = 60
Title = "MinesWeeper"

tile_numbers = []
for i in range(1, 9):
    #  pour changer le size de photo (pygame.transform.scale) avec le size de carée pour ça on mis (TileSize, TileSize)
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("Photoes", f"Tile{i}.png")), (TileSize, TileSize)))

tile_empty = (pygame.image.load(os.path.join("Photoes", f"TileEmpty.png")), (TileSize, TileSize))    
tile_exploded = (pygame.image.load(os.path.join("Photoes", f"TileExploded.png")), (TileSize, TileSize)) 
tile_flag = (pygame.image.load(os.path.join("Photoes", f"TileFlag.png")), (TileSize, TileSize)) 
tile_mine = (pygame.image.load(os.path.join("Photoes", f"TileMine.png")), (TileSize, TileSize)) 
tile_unknown = (pygame.image.load(os.path.join("Photoes", f"TileUnknown.png")), (TileSize, TileSize)) 
tile_not_mine = (pygame.image.load(os.path.join("Photoes", f"TileNotMine.png")), (TileSize, TileSize)) 