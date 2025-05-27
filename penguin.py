import pygame
pygame.init()

sc_width,sc_height=500, 500
disp_surf=pygame.display.set_mode((sc_width,sc_height))
pygame.display.set_caption('Adding image and bg image')

bg_img=pygame.transform.scale(pygame.image.load('background.png').convert(), (sc_width,sc_height))
peng_img=pygame.transform.scale(pygame.image.load('hello penguin.png').convert_alpha(), (200,200))
peng_rect=peng_img.get_rect(center=(sc_width//2,sc_height//2-30))
text=pygame.font.Font(None,36).render('Hello World', True, pygame.Color('black'))  
text_rect=text.get_rect(center=(sc_width//2,sc_height//2+110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        disp_surf.blit(bg_img, (0,0))
        disp_surf.blit(peng_img, peng_rect)
        disp_surf.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()