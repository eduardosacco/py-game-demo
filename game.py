import pygame

color_black = (0, 0, 0)
color_white = (255, 255, 255)

screen_width = 800
screen_height = 600
player_width = 35
player_height = 40

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

x = screen_width / 2 - player_width / 2
y = screen_height / 2 - player_height / 2
dx = 0
dy = 0

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        step = 30
        pressed = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -step
            elif event.key == pygame.K_LEFT:
                dx = -step
            elif event.key == pygame.K_RIGHT:
                dx = step
            elif event.key == pygame.K_DOWN:
                dy = step
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                dy = 0
            elif event.key == pygame.K_LEFT:
                dx = 0
            elif event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_DOWN:
                dy = 0

        x += dx
        y += dy

        rect = pygame.Rect(x, y, 30, 30)
        color = (0, 0, 255)
        #screen.fill(color_white)
        screen.blit(backGroundSprite, (0,0))
        screen.blit(playerSprite, (x, y))
        #pygame.draw.rect(screen, color, rect)
        pygame.display.flip()
        frame.tick(30)