import pygame
import pygame.freetype

def title_screen():
    pygame.init()

    res = (1000, 700)

    screen_color = (0, 0, 20)
    pygame.display.set_caption('Zombie Attack')
    screen = pygame.display.set_mode(res)
    
    #musica
    pygame.mixer.music.load('sounds/the_last_of_us2_music_theme.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    #sons
    bt = pygame.mixer.Sound("sounds/butons.mp3")

    #dar load à imagem
    logo = pygame.image.load("images/logo.png")
    play = pygame.image.load("images/play.png")
    sair = pygame.image.load("images/exit.png")

    while (True):
        events = pygame.event.get()

        click = False
        for event in events:
            if (event.type == pygame.QUIT):
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                
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
        
        #comandos

        pos = pygame.mouse.get_pos()

        

        button_1 = pygame.Rect(375, 400, 235, 70)
        button_2 = pygame.Rect(375, 500, 232, 70)

        if button_1.collidepoint(pos):
            if (click == True):
                bt.play()
                main()

        if button_2.collidepoint(pos):
            if click:
                bt.play()  
                exit()
                
        pygame.display.update()
        pygame.display.flip()


def main():
    pygame.init()

    res = (1000, 700)

    screen_color = (0, 0, 20)

    screen = pygame.display.set_mode(res)

    #sons

    bt = pygame.mixer.Sound("sounds/butons.mp3")
    
    #dar load à imagem
    fundo = pygame.image.load("images/fundo.png")
    zombie = pygame.image.load("characters/zombie.png")
    sair = pygame.image.load("images/exit.png")
    human = pygame.image.load("characters/human.png")


    while (True):
        #processar dos eventos 
        events = pygame.event.get()

        click = False
        for event in events:
            if (event.type == pygame.QUIT):
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

        #comandos

        pos = pygame.mouse.get_pos()


        button_3 = pygame.Rect(50,600, 235, 70)

        if button_3.collidepoint(pos):
            if click:
                bt.play()
                title_screen()
        
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



        pygame.display.update()
        pygame.display.flip()

title_screen()