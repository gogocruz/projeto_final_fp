import pygame
import pygame.freetype

def title_screen():
    pygame.init()

    res = (1000, 700)

    screen_color = (0, 0, 20)

    screen = pygame.display.set_mode(res)
    
    #musica
    pygame.mixer.music.load('the_last_of_us2_music_theme.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    #dar load à imagem
    logo = pygame.image.load("logo.png")
    play = pygame.image.load("play.png")
    sair = pygame.image.load("exit.png")

    while (True):
        events = pygame.event.get()

        for event in events:
            if (event.type == pygame.QUIT):
                exit()
        k = pygame.key.get_pressed() 
        if  k[pygame.K_ESCAPE]:
            break # colocar para abrir menu
        screen.fill(screen_color)
        screen.fill(screen_color)

        #por p fundo no ecra
        screen.blit(logo, (0,0))
        screen.blit(play, (375,400))
        screen.blit(sair, (375,500))

        pygame.display.flip()


def main():
    pygame.init()

    res = (1000, 700)

    screen_color = (0, 0, 20)

    screen = pygame.display.set_mode(res)

    #musica
    pygame.mixer.music.load('the_last_of_us2_music_theme.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    #sons
    zombie = pygame.mixer.Sound("fx1.wav")
    human= pygame.mixer.Sound("fx1.wav")
    #zombie.play() 
    # #human.play()
    
    #dar load à imagem
    fundo = pygame.image.load("fundo.png")
    zombie = pygame.image.load("zombie.png")
    human = pygame.image.load("human.png")
    sair = pygame.image.load("exit.png")

    while (True):
        #processar dos eventos 
        events = pygame.event.get()

        for event in events:
            if (event.type == pygame.QUIT):
                exit()

        #Atualizar cena
        k = pygame.key.get_pressed() 
        if  k[pygame.K_ESCAPE]:
            break # colocar para abrir menu
 
        # Desenhar 
        screen.fill(screen_color)

        #por a imagens no ecra
        screen.blit(fundo, (300,100))
        screen.blit(zombie, (350,100))
        screen.blit(zombie, (450,100))
        screen.blit(zombie, (550,100))
        screen.blit(zombie, (650,100))
        screen.blit(human, (300,450))
        screen.blit(sair, (50,600))

        #criacao do tabuleiro "fisico"
        pygame.draw.rect(screen, (200, 200, 200), (300, 100, 400, 400), 3) #borda

        #linhas verticais
        pygame.draw.line(screen, (200,200, 200), (300, 100), (300, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (350, 100), (350, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (400, 100), (400, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (450, 100), (450, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (500, 100), (500, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (550, 100), (550, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (600, 100), (600, 500), 3)
        pygame.draw.line(screen, (200,200, 200), (650, 100), (650, 500), 3)
        #linhas horizontais
        pygame.draw.line(screen, (200,200, 200), (300, 150), (700, 150), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 200), (700, 200), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 250), (700, 250), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 300), (700, 300), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 350), (700, 350), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 400), (700, 400), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 450), (700, 450), 3)
        pygame.draw.line(screen, (200,200, 200), (300, 500), (700, 500), 3)

     


        
        


        pygame.display.flip()

main()
