import pygame
import pylcanimtest as p
(width,height)=(300,200)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width,height))
pygame.display.flip()
running=True
p.init('run.sf')
while running:

    image =p.lcAnim(3,0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:

            running=False
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 50))
    pygame.display.update()

    clock.tick(60)
pygame.quit()
