import pygame
from Settings import *
from Sprites import * 

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MinsWeeper")
        self.clock = pygame.time.Clock()

    def new(self):
        pass

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS) # pour démarres l'horloge
            self.events()
            self.update()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOUR)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

game = Game()
with True:
    game.new()
    game.run()




                