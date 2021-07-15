import pygame
import functools
import random

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

screenSize = (800, 800)
playerSize = (35, 40)
treasureSize = (40, 40)
enemySize = (40, 40)

initPlayerPos = (screenSize[0] / 2 - playerSize[0] / 2, screenSize[1] * 5 / 6)
playerPos = initPlayerPos
deltaPos = (0, 0)
treasurePos = (screenSize[0] / 2 - treasureSize[0] / 2, 10)
initEnemyPos = (0, 3 / 4 * screenSize[1])
level = 1
playerStep = 10
initEnemyStep = 10
enemyStep = initEnemyStep

move_map = {
    pygame.K_w: ( 0, -1),
    pygame.K_s: ( 0,  1),
    pygame.K_a: (-1,  0),
    pygame.K_d: ( 1,  0)
}

pygame.init()
fontBig = pygame.font.SysFont("comicsans", 60)
fontSmall = pygame.font.SysFont("comicsans", 40)

textTreasure = fontBig.render("Treasure Obtained!", True, color_white)
textTreasurePos = (screenSize[0] / 2 - textTreasure.get_width() / 2, screenSize[1] / 2)

textWin = fontBig.render("You Win!!!", True, color_white)
textWinPos = (screenSize[0] / 2 - textWin.get_width() / 2, screenSize[1] / 2)

textGameOver = fontBig.render("Game Over!", True, color_white)
textGameOverPos = (screenSize[0] / 2 - textGameOver.get_width() / 2, screenSize[1] / 2)

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

enemySprite = pygame.image.load("./assets/enemy.png")
enemySprite = pygame.transform.scale(enemySprite, enemySize)
enemySprite = enemySprite.convert()

enemyNames = { 0 : "Bob", 1 : "Nigel", 2 : "Sarah", 3 : "Chris", 5 : "Lula" }
enemies = [(initEnemyPos, True)]

frame =  pygame.time.Clock()

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
        pressed = pygame.key.get_pressed()
        move = [move_map[key] for key in move_map if pressed[key]]
        direction = functools.reduce(tupleAdd, move, (0, 0))

        if direction != (0, 0):
            deltaPos = tuple([playerStep * x for x in direction])
            playerPos = tupleAdd(playerPos, deltaPos)

        # enemy movement and collisions
        enemyColision = False
        enemyIndex = 0
        enemyCollided = None
        for enemyPos, movingRight in enemies:
            if enemyPos[0] >= screenSize[0] - enemySize[0]:
                movingRight = False
            elif enemyPos[0] <= 0:
                movingRight = True

            if movingRight:
                enemyPos = tupleAdd(enemyPos, (enemyStep, 0))
            else:
                enemyPos = tupleAdd(enemyPos, (-enemyStep, 0))
            
            enemies[enemyIndex] = (enemyPos, movingRight)
            enemyColision = checkCollision(playerPos, playerSize, enemyPos, enemySize)
            if enemyColision:
                enemyCollided = enemyIndex
                break

            enemyIndex += 1     

        if enemyColision:
            screen.blit(textGameOver, textGameOverPos)
            subtextGameOver = fontSmall.render("You were stomped by " + enemyNames[enemyCollided], True, color_white)
            subtextGameOverPos = (screenSize[0] / 2 - subtextGameOver.get_width() / 2, screenSize[1] / 2 + textGameOver.get_height() + 10)
            screen.blit(subtextGameOver, subtextGameOverPos)
            level = 1
            enemyStep = initEnemyStep
            textLevel = fontSmall.render("Level: " + str(level), True, color_white)
            pygame.display.flip()
            frame.tick(1)
            playerPos = initPlayerPos
            del enemies[1:]

        # take into account order of drawing 
        screen.blit(backgroundSprite, (0,0))
        screen.blit(textLevel, textLevelPos)
        screen.blit(playerSprite, playerPos)
        for enemyPos, movingRight in enemies:
            screen.blit(enemySprite, enemyPos)
        screen.blit(treasureSprite, treasurePos)

        treasureCollision = checkCollision(playerPos, playerSize, treasurePos, treasureSize)
        if treasureCollision:
            screen.blit(textTreasure, textTreasurePos)
            enemies.append(((initEnemyPos[0] - random.randint(10, 50), initEnemyPos[1] - level * 3 * enemySize[1]),
                bool(random.getrandbits(1))))
            level += 1
            enemyStep += 2 * level
            textLevel = fontSmall.render("Level: " + str(level), True, color_white)
            pygame.display.flip()
            frame.tick(1)
            playerPos = initPlayerPos

            if level > 5:
                screen.blit(textWin, textWinPos)
                pygame.time.wait(5)
                finished = True

        pygame.display.flip()
        frame.tick(30)