import pygame
pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption("My game")
pygame.display.set_icon(pygame.image.load("src/images/pacman-icon.webp"))
speed = [2, 2]
black = (0, 0, 0)

ball = pygame.image.load("src/images/intro_ball.gif")
ballrect = ball.get_rect()

FPS = 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

            
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.update()
    
    clock.tick()