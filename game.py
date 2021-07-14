import pygame
import functools

def tupleAdd(x, y):
    return (x[0] + y[0], x[1] + y[1])

color_black = (0, 0, 0)
color_white = (255, 255, 255)

screen_width = 800
screen_height = 600
player_width = 35
player_height = 40

move_map = {
    pygame.K_UP: ( 0, -1),
    pygame.K_DOWN: ( 0,  1),
    pygame.K_LEFT: (-1,  0),
    pygame.K_RIGHT: ( 1,  0)
}

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
finished = False

playerSprite = pygame.image.load("./assets/player.png")
playerSprite = pygame.transform.scale(playerSprite, (player_width, player_height))
playerSprite = playerSprite.convert()

backGroundSprite = pygame.image.load("./assets/background.png")
backGroundSprite = pygame.transform.scale(backGroundSprite, (screen_width, screen_height))
backGroundSprite = backGroundSprite.convert()

frame =  pygame.time.Clock()

pos = (screen_width / 2 - player_width / 2, screen_height / 2 - player_height / 2)
delta = (0, 0)

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        step = 30
        pressed = pygame.key.get_pressed()
        move = [move_map[key] for key in move_map if pressed[key]]
        direction = functools.reduce(tupleAdd, move, (0, 0))

        print(direction * step)
        if direction != (0, 0):
            delta = tuple([step * x for x in direction])
            pos = tupleAdd(pos, delta)

        screen.blit(backGroundSprite, (0,0))
        screen.blit(playerSprite, pos)
        pygame.display.flip()
        frame.tick(30)