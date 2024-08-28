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
        
        ## window size which can be adjusted adjusted independently
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))

        # GAMESPACE DISPLAY can be adjusted adjusted independently
        self.display = pygame.Surface((areaSize,  screenHeight)) 
        self.guiDisplay = pygame.Surface((guiSize, screenHeight))

        self.clock = pygame.time.Clock()
        self.movement = [False, False, False, False]

        ## IMAGE INIT IS INSIDE THE PLANE
        self.plane = TopDownEntity(self, 'player', playerPos, (1,1),'misc/img/pl1.png') 

        self.gameSpace = GameArea(self.display)
        self.bg = pygame.image.load('misc/img/bg.png')

        self.font = pygame.font.SysFont('calibri', 30, italic = False, bold = False)

    def run(self) -> None:
        while True:
            self.display.blit(self.bg, (0,0))
            self.gameSpace.InSpace()

            # movement update
            self.plane.update((self.movement[1] - self.movement[0],
                               self.movement[3] - self.movement[2]))
            self.plane.render(self.display) ## Render the plane in the Game Space


            # Just example in GUI
            self.guiDisplay.fill((0 ,0 ,255)) #Display blue on this area
            self.text = self.font.render(f"Position: {self.plane.pos}", True, (255,255,255))
            self.guiDisplay.blit((self.text), (0,0))
            

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


            self.screen.blit(self.display, (0, 0)) ## Render the gamespace inside the window
            self.screen.blit(self.guiDisplay, guiPosition) ## Render GUI Space inside the screen window
            pygame.display.update()
            self.clock.tick(30)
    

Game().run()