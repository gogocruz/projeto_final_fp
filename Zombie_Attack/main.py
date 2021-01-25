import pygame 
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

# !!Functions! #

# Load the images 
def loadImages(): #dar load à imagem
    players=["human", "zombie"]
    for player in players:
        images[player]= pygame.transform.scale(pygame.image.load("characters/"+ player + ".png"),(square_size,square_size))

#highlight the next valid positions
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

#Draw all the game board 
def drawBoard(screen):
    fundo = pygame.transform.scale(pygame.image.load("images/fundo.png"),(700,700))
    screen.blit(fundo, (0,0))
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 700, 700), 3) #Square that completes the board 

    for j in range(dimension):
        pygame.draw.line(screen, (200,200, 200), ((square_size*j), 0), ((square_size*j), 700), 3)
        pygame.draw.line(screen, (200,200, 200), (0, (square_size*j)), (700,(square_size*j)), 3)

#Draw the images to the game board            
def drawPlayers(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            player = board[r][c]
            if player != "--":
                screen.blit(images[player],pygame.Rect( (c*square_size), (r*square_size),square_size,square_size))
#END of Functions


#Title Screen
def title_screen():
    # Initialize pygame, with the default parameters
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(screen_color)

    # Initialize the game music
    pygame.mixer.music.load('sounds/the_last_of_us2_music_theme.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    #Initialize the butons sound and load them
    bt = pygame.mixer.Sound("sounds/butons.mp3")
    logo = pygame.image.load("images/logo.png")
    play = pygame.image.load("images/play.png")
    sair = pygame.image.load("images/exit.png")

    # Game loop, runs forever
    while (True):
        # Process OS events
        events = pygame.event.get()
        click = False
        for event in events:
            if (event.type == pygame.QUIT):
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

        # Load and place the butons
        screen.blit(logo, (0,0))
        screen.blit(play, (375, 400))
        screen.blit(sair, (375, 500))

        # Click bos of the exit and play butons
        button_1 = pygame.Rect(375, 400, 235, 70)
        button_2 = pygame.Rect(375, 500, 232, 70)

        #Get mouse position
        pos = pygame.mouse.get_pos()

        if button_1.collidepoint(pos):
            if (click == True):
                bt.play()
                main()

        if button_2.collidepoint(pos):
            if click:
                bt.play()
                exit()

        #keeps the display updated
        pygame.display.update()
        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


#Game Screen
def main():

    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window with the values of widht and height
    screen = pygame.display.set_mode((width,height))
    # Clears the screen with a very dark blue (0, 0, 20)
    screen_color = (0, 0, 20)
    screen.fill(screen_color)
    #Create a clock to track an amount of time
    clock =pygame.time.Clock()

    #Seting the Gamestate class to the variable gs
    gs = setting.GameState()
    
    #Seting the getValidMoves function to the variable validMoves
    validMoves = gs.getValidMoves()
    # Set move made and game over to default False value
    moveMade = False
    GameOver = False
    #Load the images to the screen
    loadImages()
    #Variable that keeps the Game loop to runs forever
    running= True

    sqSelected = () #to keep the track of last click of user(one tuple)
    playerClicks =[] # keep the track of player clicks(two tuple)

    #Loaf the buton of exit and it  sound
    sair = pygame.image.load("images/exit.png")
    bt = pygame.mixer.Sound("sounds/butons.mp3")
    
    while (running):

        #Setting the pygame.event to the variable events
        events = pygame.event.get() 
        #Setting the mouse position 
        pos = pygame.mouse.get_pos()
        #Setting the colision bos to this coordinates with the variable button_3
        button_3 = pygame.Rect(740,600, 235, 70)

        # Process OS events 
        click = False
        for event in events:
            if (event.type == pygame.QUIT):
                # Checks if the user closed the window
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Checks the user mouse clicks with his location in x and y
                    location = pygame.mouse.get_pos() # (x, y) location of mouse
                    col = (location[0]//square_size)
                    row = (location[1]//square_size)
                    #Check if the player cick woth the left buton of the mouse
                    if event.button == 1:
                        click = True
                    #Until is not game over
                    if not GameOver:
                        try:
                            if sqSelected == (row , col): # user clicked the same square twice
                                sqSelected = () #deselect
                                playerClicks = [] #clear playerclick

                            else:
                                sqSelected = (row , col)
                                playerClicks.append(sqSelected) # append for both 1st and 2nd clicks 
                            #Put the clisk in a list with the value of 2
                            if len(playerClicks) == 2: # after 2nd click
                                #Turning the two clicks into a move
                                move = setting.Move(playerClicks[0],playerClicks[1], gs.board)
                                #Checking if two clicks are a move
                                for i in range(len(validMoves)):
                                    if move == validMoves[i]:
                                        gs.makeMove(validMoves[i])
                                        moveMade = True
                                        sqSelected = ()
                                        playerClicks = []
                                #If not is not a valid move clears the list of clicks       
                                if not moveMade:
                                    sqSelected = ()
                                    playerClicks = []
                        #If nothing above as been read, pass            
                        except:
                            pass
        #If the clicks are inside the game board and dont make valid move, then no move motivated                
        if moveMade:
            validMoves= gs.getValidMoves()
            moveMade = False
        #Check ig the exit button  is clicked
        if button_3.collidepoint(pos):
            if (click == True):
                bt.play()
                title_screen()
        #LOad to the screen the exit buton     
        screen.blit(sair, (740,600))
        #Check if is any win condition
        if gs.humanWin or gs.zombieWin:
            GameOver = True
            
        drawGameState(screen,gs, validMoves, sqSelected)
        #Set the amount of time to the variable FPS wich is 60
        clock.tick(FPS) 
        # Swaps the back and front buffer, effectively displaying what we rendered   
        pygame.display.flip()

#Calling the title screen to something apear :D
title_screen()
