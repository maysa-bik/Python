import pygame
from jeu import Jeu

def main():
    pygame.init()
    jeu = Jeu()
    jeu.nouveau()
    jeu.run()
    pygame.quit()

if __name__ == "__main__":
    main()
