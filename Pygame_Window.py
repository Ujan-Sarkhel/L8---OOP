import pygame
pygame.init()
sc=pygame.display.set_mode((400,500))

i=False
while not i:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()