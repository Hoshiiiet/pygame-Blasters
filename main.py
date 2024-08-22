import pygame
import sys

#VARIABLES
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
screenWidth = 480
screenHeight = 640
colSize = 288
space = 256

def main():
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_caption("Blasters")
    SCREEN = pygame.display.set_mode((screenWidth, screenHeight))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    #player varibales
    p_icon = pygame.image.load('misc/img/pl1.png')
    playerRect = p_icon.get_rect()
    playerRect.x = 128
    playerRect.y = 575
    playerRect.center = (playerRect.x, playerRect.y)
    playerX = [False, False]
    playerY = [False, False]

    #bg
    bg = pygame.image.load('misc/img/bg.png')

    while True:
        SCREEN.blit(bg, (0, 0))
        SCREEN.blit(p_icon, playerRect.center)
        gameArea()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: playerY[0] = True
                if event.key == pygame.K_s: playerY[1] = True
                if event.key == pygame.K_a: playerX[0] = True
                if event.key == pygame.K_d: playerX[1] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w: playerY[0] = False
                if event.key == pygame.K_s: playerY[1] = False
                if event.key == pygame.K_a: playerX[0] = False
                if event.key == pygame.K_d: playerX[1] = False

            if (playerRect.right >= 268):
                playerX[1] = False
            if (playerRect.left <= 0):
                playerX[0] = False
            if (playerRect.top <= 0):
                playerY[0] = False
            if (playerRect.bottom >= 600):
                playerY[1] = False

        if (playerX[0] or playerX[1]):
            playerRect.x += (playerX[1] - playerX[0]) * 7
        if (playerY[0] or playerY[1]):
            playerRect.y += (playerY[1] - playerY[0]) * 7

        pygame.display.flip()
        CLOCK.tick(20)


def gameArea():
    for x in range(0, space, colSize):
        area = pygame.Rect(x, 0, colSize, screenHeight)
        pygame.draw.rect(SCREEN, WHITE, area, 1)
           

#GAME
main()