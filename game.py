import pygame
import functools

def tupleAdd(x, y):
    return (x[0] + y[0], x[1] + y[1])

def checkCollision(a, aSize, b, bSize):
    # player collision with treasure caveman version
    # this way of collision checking may not work depending on the size of objects 
    xCollision = False
    yCollision = False

    if (a[1] >= b[1] and a[1] <= b[1] + bSize[1] or
        a[1] + aSize[1] >= b[1] and a[1] + aSize[1] <= b[1] + bSize[1]):
        yCollision = True
    if (a[0] + aSize[0] >= b[0] and a[0] <= b[0] + bSize[0] or 
        a[0] + aSize[0] >= b[0] and a[0] + aSize[0] <= b[0] + bSize[0]):
        xCollision = True

    if xCollision and yCollision:
        return True
    else:
        return False

color_black = (0, 0, 0)
color_white = (255, 255, 255)

screenSize = (800, 600)
playerSize = (35, 40)
treasureSize = (40, 40)

initPlayerPos = (screenSize[0] / 2 - playerSize[0] / 2, screenSize[1] * 3 / 4)
playerPos = initPlayerPos
deltaPos = (0, 0)
treasurePos = (screenSize[0] / 2 - treasureSize[0] / 2, screenSize[1] / 4)
level = 1

move_map = {
    pygame.K_UP: ( 0, -1),
    pygame.K_DOWN: ( 0,  1),
    pygame.K_LEFT: (-1,  0),
    pygame.K_RIGHT: ( 1,  0)
}

pygame.init()
fontBig = pygame.font.SysFont("comicsans", 60)
fontSmall = pygame.font.SysFont("comicsans", 40)
textWin = fontBig.render("Treasure Obtained!", True, color_white)
textWinPos = (screenSize[0] / 2 - textWin.get_width() / 2, screenSize[1] / 2)
textLevel = fontSmall.render("Level: " + str(level), True, color_white)
textLevelPos = (0, 0)
screen = pygame.display.set_mode(screenSize)
finished = False

playerSprite = pygame.image.load("./assets/player.png")
playerSprite = pygame.transform.scale(playerSprite, playerSize)
playerSprite = playerSprite.convert()

backgroundSprite = pygame.image.load("./assets/background.png")
backgroundSprite = pygame.transform.scale(backgroundSprite, screenSize)
backgroundSprite = backgroundSprite.convert()

treasureSprite = pygame.image.load("./assets/treasure.png")
treasureSprite = pygame.transform.scale(treasureSprite, treasureSize)
treasureSprite = treasureSprite.convert()

frame =  pygame.time.Clock()

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        step = 10
        pressed = pygame.key.get_pressed()
        move = [move_map[key] for key in move_map if pressed[key]]
        direction = functools.reduce(tupleAdd, move, (0, 0))

        if direction != (0, 0):
            deltaPos = tuple([step * x for x in direction])
            playerPos = tupleAdd(playerPos, deltaPos)

        # take into account order of drawing 
        screen.blit(backgroundSprite, (0,0))
        screen.blit(textLevel, textLevelPos)
        screen.blit(playerSprite, playerPos)
        screen.blit(treasureSprite, treasurePos)

        collision = checkCollision(playerPos, playerSize, treasurePos, treasureSize)
        if collision:
            screen.blit(textWin, textWinPos)
            level += 1
            textLevel =  fontSmall.render("Level: " + str(level), True, color_white)
            pygame.display.flip()
            frame.tick(1)
            playerPos = initPlayerPos

        pygame.display.flip()
        frame.tick(30)