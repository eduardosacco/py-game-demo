import pygame
import functools

def tupleAdd(x, y):
    return (x[0] + y[0], x[1] + y[1])

color_black = (0, 0, 0)
color_white = (255, 255, 255)

screen_size = (800, 600)
player_size = (35, 40)
treasure_size = (30, 30)

move_map = {
    pygame.K_UP: ( 0, -1),
    pygame.K_DOWN: ( 0,  1),
    pygame.K_LEFT: (-1,  0),
    pygame.K_RIGHT: ( 1,  0)
}

pygame.init()
screen = pygame.display.set_mode(screen_size)
finished = False

playerSprite = pygame.image.load("./assets/player.png")
playerSprite = pygame.transform.scale(playerSprite, player_size)
playerSprite = playerSprite.convert()

backgroundSprite = pygame.image.load("./assets/background.png")
backgroundSprite = pygame.transform.scale(backgroundSprite, screen_size)
backgroundSprite = backgroundSprite.convert()

treasureSprite = pygame.image.load("./assets/treasure.png")
treasureSprite = pygame.transform.scale(treasureSprite, treasure_size)
treasureSprite = treasureSprite.convert()

frame =  pygame.time.Clock()

playerPos = (screen_size[0] / 2 - player_size[0] / 2, screen_size[1] / 2 - player_size[1] / 2)
deltaPos = (0, 0)

treasurePos = (screen_size[0] / 2 - treasure_size[0] / 2, screen_size[1] / 4)

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        step = 30
        pressed = pygame.key.get_pressed()
        move = [move_map[key] for key in move_map if pressed[key]]
        direction = functools.reduce(tupleAdd, move, (0, 0))

        if direction != (0, 0):
            deltaPos = tuple([step * x for x in direction])
            playerPos = tupleAdd(playerPos, deltaPos)

        screen.blit(backgroundSprite, (0,0))
        screen.blit(playerSprite, playerPos)
        screen.blit(treasureSprite, treasurePos)
        pygame.display.flip()
        frame.tick(30)