import pygame
pygame.init()
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")
image = pygame.image.load("32820e98-5272-4613-a48f-75827706a2a4.png")
image = pygame.transform.scale(image, (300, 300))
x = (window_size[0] - 300) // 2
y = (window_size[1] - 300) // 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((58, 58, 58))              
    screen.blit(image, (x, y))             
    pygame.display.update()                
pygame.quit()
