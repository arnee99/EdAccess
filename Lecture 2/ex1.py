import pygame
pygame.init()

pygame.display.set_mode((600,400))
speed = [2, 2]
black = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()