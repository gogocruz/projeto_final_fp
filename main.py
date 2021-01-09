import pygame
import pygame.freetype

def main():
    pygame.init()

    res = (1000, 700)

    screen_color = (0, 0, 20)

    screen = pygame.display.set_mode(res)

    #dar load à imagem
    #image = pygame.image.load("nome.png")

    while (True):
        events = pygame.event.get()

        for event in events:
            if (event.type == pygame.QUIT):
                exit()

        screen.fill(screen_color)

        #por a imagem no ecra
        #screen.blit(image, (0,0))

        pygame.draw.rect(screen, (0, 255, 0), (300, 100, 400, 400), 3)

        pygame.draw.line(screen, (0,255, 0), (300, 100), (300, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (350, 100), (350, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (400, 100), (400, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (450, 100), (450, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (500, 100), (500, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (550, 100), (550, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (600, 100), (600, 500), 3)
        pygame.draw.line(screen, (0,255, 0), (650, 100), (650, 500), 3)

        pygame.draw.line(screen, (0,255, 0), (300, 150), (700, 150), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 200), (700, 200), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 250), (700, 250), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 300), (700, 300), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 350), (700, 350), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 400), (700, 400), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 450), (700, 450), 3)
        pygame.draw.line(screen, (0,255, 0), (300, 500), (700, 500), 3)

     


        
        


        pygame.display.flip()

main()
