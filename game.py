import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))
finished = False

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        rect = pygame.Rect(0, 0, 30, 40)
        color = (0, 0, 255)
        pygame.draw.rect(screen, color, rect)
        pygame.display.flip()