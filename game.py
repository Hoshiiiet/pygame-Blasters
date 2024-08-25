import sys
import pygame
import config

from config import *
from scripts.gameScreen import GameArea
from scripts.entity import TopDownEntity # Referenes from Entity Class

class Game :
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption('Blasters')
        self.screen = pygame.display.set_mode((screenWidth, screenHeight)) 
        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]

        self.plane = TopDownEntity(self, 'player', playerPos, (1,1))
        self.gameSpace = GameArea(self.screen)

        self.bg = pygame.image.load('misc/img/bg.png')
        self.plane_icon = pygame.image.load('misc/img/pl1.png')
        self.iconRect = self.plane_icon.get_rect()
        self.iconRect.center = playerPos


    def run(self) -> None:
        while True:
            # movement update
            self.plane.update((self.movement[1] - self.movement[0],
                               self.movement[3] - self.movement[2]))
            
            self.screen.blit(self.bg, (0,0))
            self.screen.blit(self.plane_icon, self.plane.pos)

            self.gameSpace.InSpace()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:                        
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True

                elif event.type == pygame.KEYUP :
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(30)


Game().run()