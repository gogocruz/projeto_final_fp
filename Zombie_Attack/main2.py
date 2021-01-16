import pygame 
import pygame.freetype
import setting


#Variables
height = 700
width = 1000
dimension = 8
FPS=60
square_size = height // dimension
screen_color = (0, 0, 20)
images ={}
#END of Variables

#NAME AND ICON OF THE GAME
pygame.display.set_caption('Zombie Attack') 
icon = pygame.image.load('characters/human.png') 
pygame.display.set_icon(icon)

#Functions 
def loadImages(): #dar load à imagem
    players=["human", "zombie"]
    for player in players:
        images[player]= pygame.transform.scale(pygame.image.load("characters/"+ player + ".png"),(square_size,square_size))

def highlightSquares(screen, gs, validMoves, sqSelected):

    if sqSelected != ():
        r, c = sqSelected
        try : 
            if gs.board [r][c][0] == ('h' if gs.humanToMove else 'z'):
                s = pygame.Surface((square_size, square_size))
                s.set_alpha(50)
                s.fill(pygame.Color('white'))
                screen.blit(s, (c*square_size, r*square_size))
                s.fill(pygame.Color('yellow'))
            for move in  validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol*square_size, move.endRow*square_size))
        except:
            pass


def drawGameState(screen,gs, validMoves, sqSelected):
    drawBoard(screen)
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPlayers(screen,gs.board)

def drawBoard(screen):

    fundo = pygame.transform.scale(pygame.image.load("images/fundo.png"),(700,700))
    screen.blit(fundo, (0,0))
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 700, 700), 3)    #Square that completes the board 

    for j in range(dimension):
        pygame.draw.line(screen, (200,200, 200), ((square_size*j), 0), ((square_size*j), 700), 3)
        pygame.draw.line(screen, (200,200, 200), (0, (square_size*j)), (700,(square_size*j)), 3)
            
def drawPlayers(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            player = board[r][c]
            if player != "--":
                screen.blit(images[player],pygame.Rect( (c*square_size), (r*square_size),square_size,square_size))


#END of Functions


#Title Screen
def title_screen():

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(screen_color)

    #musica
    pygame.mixer.music.load('sounds/the_last_of_us2_music_theme.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    #sons
    bt = pygame.mixer.Sound("sounds/butons.mp3")

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
            

        #por p fundo no ecra
        screen.blit(logo, (0,0))
        screen.blit(play, (375, 400))
        screen.blit(sair, (375, 500))

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


#Game Screen
def main():
    pygame.init()
    screen_color = (0, 0, 20)
    screen = pygame.display.set_mode((width,height))
    clock =pygame.time.Clock()
    screen.fill(screen_color)
    gs = setting.GameState()

    validMoves = gs.getValidMoves()
    moveMade = False

    loadImages()
    running= True
    sqSelected = () #to keep the track of last click of user(one tuple)
    playerClicks =[] # keep the track of player clicks(two tuple)
    #sair = pygame.image.load("images/exit.png")


    while (running):
        #processar dos eventos 
        events = pygame.event.get() 
        for event in events:
            if (event.type == pygame.QUIT):
                exit()
            # mouse button Functions
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # (x, y) location of mouse
                col = (location[0]//square_size)
                row = (location[1]//square_size)

                if sqSelected == (row , col): # user clicked the same square twice
                    sqSelected = () #deselect
                    playerClicks = [] #clear playerclick

                else:
                    sqSelected = (row , col)
                    playerClicks.append(sqSelected) # append for both 1st and 2nd clicks   

                if len(playerClicks) == 2: # after 2nd click
                    move = setting.Move(playerClicks[0],playerClicks[1], gs.board)

                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = ()
                        playerClicks= []

                    if moveMade:
                        validMoves= gs.getValidMoves()
                        moveMade = False

                        
    #pos = pygame.mouse.get_pos()
    #button_3 = pygame.Rect(740,600, 235, 70)

    #if button_3.collidepoint(pos):
    #    if click:
    #        bt.play()
    #        title_screen()
    #    screen.blit(sair, (740,600))

        drawGameState(screen,gs, validMoves, sqSelected)
        clock.tick(FPS)    
        pygame.display.flip()

title_screen()