import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.score = score
        self.add(group)
        
    def update(self, *args):
        if self.rect.y < args[0]-20:
            self.rect.y += self.speed
        else:
            # self.rect.y = 0
            self.kill()