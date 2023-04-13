import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption("Tori's game")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_i:
                        self.level.inventory_show()
            self.screen.fill('black')
            self.level.run()
            #debug('hello')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
