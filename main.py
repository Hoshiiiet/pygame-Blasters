import pygame
import sys

#VARIABLES
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
screenWidth = 480
screenHeight = 640

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
    currentPos = [128, 575]

    #bg
    bg = pygame.image.load('misc/img/bg.png')

    #movement variables
    xmovement = [False, False]
    ymovement = [False, False]

    while True:

        currentPos[0] += (xmovement[1] - xmovement[0]) * 7
        currentPos[1] += (ymovement[1] - ymovement[0]) * 7

        SCREEN.blit(bg, (0, 0))
        SCREEN.blit(p_icon, currentPos)
        drawCol()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ymovement[0] = True
                if event.key == pygame.K_s:
                    ymovement[1] = True
                if event.key == pygame.K_a:
                    xmovement[0] = True
                if event.key == pygame.K_d:
                    xmovement[1] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    ymovement[0] = False
                if event.key == pygame.K_s:
                    ymovement[1] = False
                if event.key == pygame.K_a:
                    xmovement[0] = False
                if event.key == pygame.K_d:
                    xmovement[1] = False

        pygame.display.flip()
        CLOCK.tick(15)


def drawCol():
    colSize = 288
    space = 256

    for x in range(0, space, colSize):
        area = pygame.Rect(x, 0, colSize, screenHeight)
        pygame.draw.rect(SCREEN, WHITE, area, 1)
           

#GAME
main()