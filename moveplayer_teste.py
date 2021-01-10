import pygame
import pygame.freetype

def title_screen():
    pygame.init()

    res = (1000, 700)

    screen_color = (0, 0, 20)
    pygame.display.set_caption('Zombie Attack')
    screen = pygame.display.set_mode(res)
    
    #Music
    pygame.mixer.music.load('sounds/the_last_of_us2_music_theme.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    #Sounds
    bt = pygame.mixer.Sound("sounds/butons.mp3")

    #Load Images
    logo = pygame.image.load("img/logo.png")
    play = pygame.image.load("img/play.png")
    sair = pygame.image.load("img/exit.png")

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
            break

        screen.fill(screen_color)
        screen.fill(screen_color)

        #por p fundo no ecra
        screen.blit(logo, (0,0))
        screen.blit(play, (375,400))
        screen.blit(sair, (375,500))

        pygame.display.flip()

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

    #Sounds

    bt = pygame.mixer.Sound("sounds/butons.mp3")
    
    #Image Load
    fundo = pygame.image.load("img/fundo.png")
    zombies = pygame.image.load("img/zombie.png")
    humans = pygame.image.load("img/human.png")
    sair = pygame.image.load("img/exit.png")
    
    def tabuleiro():
            #criacao do tabuleiro "fisico"

            pygame.draw.rect(screen, (200, 200, 200), (300, 100, 400, 400), 3) #limites
            win_line = pygame.draw.line(screen, (0,255, 0), (300, 100), (700, 100), 3)
            #if (human_pos in win_line):

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

    #Human player
    class Human:
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.player = pygame.image.load("img/human.png")
            self.rect = self.player.get_rect(topleft=(x, y))

        def load(self):
            screen.blit(self.player, self.rect)

        def move_upright(self):
            self.x += 50
            self.y -= 50
            self.rect.x = self.x
            self.rect.y = self.y

        def move_upleft(self):
            self.x -= 50
            self.y -= 50
            self.rect.x = self.x
            self.rect.y = self.y

        def move_down_right(self):
            self.x += 50
            self.y += 50
            self.rect.x = self.x
            self.rect.y = self.y

        def move_down_left(self):
            self.x -= 50
            self.y += 50
            self.rect.x = self.x
            self.rect.y = self.y

        def next_move(self,human, y,x):
            self.tabuleiro[human.x][human.y], self.tabuleiro[x][y] = self.tabuleiro[x][y], self.tabuleiro[human.x][human.y]
            human.move(x,y)

    def get_human(self,x,y):
        return self.tabuleiro[x][y]


    def get_move_from_mouse(pos):
        x,y = pos
        x = y // tabuleiro
        u = x // tabuleiro
        return x,y

        
    #Zombie playerm
    class Zombie:
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.player = pygame.image.load("img/zombie.png")
            self.rect = self.player.get_rect(topleft=(x, y))

        def load(self):
            screen.blit(self.player, self.rect)

        def move_down_right(self):
            self.x += 50
            self.y += 50
            self.rect.x = self.x
            self.rect.y = self.y

        def move_down_left(self):
            self.x -= 50
            self.y += 50
            self.rect.x = self.x
            self.rect.y = self.y


    while (True):
        #event processing 
        events = pygame.event.get()

        click = False
        for event in events:
            if (event.type == pygame.QUIT):
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x,y = get_move_from_mouse(pos)
                human = tabuleiro.get_human(x, y)


        #comands
        pos = pygame.mouse.get_pos()


        button_3 = pygame.Rect(50,600, 235, 70)

        if button_3.collidepoint(pos):
            if click:
                bt.play()
                title_screen()
        
        #Scene Refresh
        k = pygame.key.get_pressed() 
        if  k[pygame.K_ESCAPE]:
            break
 
        # Draw 
        screen.fill(screen_color)

        #por a imagens no ecra
        screen.blit(fundo, (300,100))
        screen.blit(zombies, (350,100))
        screen.blit(zombies, (450,100))
        screen.blit(zombies, (550,100))
        screen.blit(zombies, (650,100))
        screen.blit(humans, (300,450))
        screen.blit(sair, (50,600))

        tabuleiro()
        pygame.display.update()
        pygame.display.flip()

title_screen()
