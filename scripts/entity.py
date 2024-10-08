import pygame
from config import *

# Used for making entity

class TopDownEntity :
    def __init__(self, game, e_type, pos, size) -> None:
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = 4

    def update(self, movement = (0, 0)): ## updates movement
        moveX = movement[0] * self.velocity
        moveY = movement[1] * self.velocity
        frame_movement = (moveX, moveY) # (X, Y)
    
        new_pos = (self.pos[0] + frame_movement[0], self.pos[1] + frame_movement[1])
        bounded_pos = self.boundary(new_pos[0], new_pos[1])  # Call the boundary function
        self.pos = bounded_pos

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)

    def boundary(self, xMove, yMove):
        xPos = min(max(5, xMove), areaSize - playerWidth - 5)
        yPos = min(max(5, yMove), screenHeight - playerHeight - 5)

        return xPos, yPos
