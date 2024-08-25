import pygame


from config import *

class GameArea:
    def __init__(self, screen) -> None:
        self.window = screen

    def InSpace(self) -> None:
        for x in range(0, space, areaSize):
            area = pygame.Rect(x, 0, areaSize, screenHeight)
            pygame.draw.rect(self.window, WHITE, area, 5)