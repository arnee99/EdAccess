import pygame
from random import randint
from ball import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)
# print(pygame.USEREVENT)

BLACK = (0, 0, 0)
# 1282  x  723
W, H = 1280, 720
sc = pygame.display.set_mode((W, H))

#Audio effects
pygame.mixer.music.load('audio/crowd.mp3')
pygame.mixer.music.play(-1)
hit = pygame.mixer.Sound('audio/hit.mp3')
boo = pygame.mixer.Sound('audio/boo.mp3')
nice = pygame.mixer.Sound('audio/nice.mp3')


# clock = pygame.time.Clock()

player = pygame.image.load('images/baseball-player.webp').convert_alpha()
player = pygame.transform.scale(player, (256,256))
player_rect = player.get_rect(centerx = W//2, centery = H-130)

balls_data = ({'path': 'baseball.png', 'score': 100},
              {'path': 'basketball.png', 'score': 0},
              {'path': 'volleyball.png', 'score': 0},
              {'path': 'football.png', 'score': 0})


# balls_images = ['basketball.png', 'football.png', 'volleyball.png', 'baseball.png']
balls_surf = [pygame.image.load('images/' + data['path']).convert_alpha() 
              for data in balls_data]

def createBall(group):
    # index of the ball
    indx = randint(0, len(balls_surf)-1)
    # initial position of X
    x = randint(20, W-20)
    speed = randint(1, 4)
    
    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

game_score = 0

def collideBalls():
    global game_score
    for ball in balls:
        if player_rect.collidepoint(ball.rect.center):
            if ball.score == 0:
                boo.play()
            else:
                hit.play()
                nice.play()
            game_score += ball.score
            ball.kill()

balls = pygame.sprite.Group()

bg = pygame.image.load('images/bg.webp').convert()

speed = 10

createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
        if player_rect.x < 0:
            player_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        player_rect.x += speed
        if player_rect.x > W-player_rect.width:
            player_rect.x = W-player_rect.width
            
    collideBalls()        
            
    sc.fill(BLACK)
    sc.blit(bg, (0, 0))
    balls.draw(sc)
    sc.blit(player, player_rect)
    
    pygame.display.update()
    pygame.time.Clock().tick(60)
    balls.update(H)