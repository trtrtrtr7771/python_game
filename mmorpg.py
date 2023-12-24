import pygame
from sys import exit

pygame.init()


clock = pygame.time.Clock()

screen = pygame.display.set_mode((700,600))

text_font = pygame.font.SysFont("pixel", 53)
def  draw_txt(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    pass

#pygame.display.set_caption('main')

def menue():
    
    pygame.display.set_caption('main menue')
    while True:
        screen.fill("purple") 
        
        draw_txt("press space to play", text_font, (255, 255, 255, 255), 248, 300)
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        key = pygame.key.get_pressed()
        if key [pygame.K_SPACE]:
            main()
                  
        pygame.display.flip()
        clock.tick(60)
            

def main():
    
    pl_x = 100
    pl_y = 100
    box_color = (255, 0, 0, 0)
    box_size = 20

    while True:

        screen.fill("white")
        
        pygame.draw.rect(screen, box_color, (pl_y, pl_x, box_size, box_size))
        

            
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        key = pygame.key.get_pressed()
        if key [pygame.K_w]:
            pl_x -= 1.5
        if key [pygame.K_s]:
            pl_x +=1.5
        if key [pygame.K_a]:
            pl_y -= 1.5
        if key [pygame.K_d]:
            pl_y += 1.5
        
        pygame.display.flip()
        clock.tick(60)
        
        
        
menue()