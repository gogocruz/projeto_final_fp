import pygame 
#Load the images of Win
humanwin = pygame.image.load("images/humanwins.png")
zombiewin = pygame.image.load("images/zombieswin.png")

#Class wich is checking all the game state
class GameState():

    def __init__(self):
        #Setting the  gameboard into a matris with the starting location of the characters 
        self.board = [
            ["--","zombie","--","zombie","--","zombie","--","zombie"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","human","--","--","--"]
        ]
        #Seeting the first turn ro human(sheep)
        self.humanToMove = True
        #Turn the win conditions to false
        self.humanWin = False
        self.zombieWin = False

    #Make movement    
    def makeMove(self, move):
        #Check if the next square is empty 
        self.board[move.startRow][move.startCol] = "--"
        #If yes load the new movemnt
        self.board[move.endRow][move.endCol] = move.playerMoved
        #
        self.humanToMove = not self.humanToMove
        #IF the human reach the first line its human win
        if move.gameover:
            #Turning the human win true
            self.humanWin = True         
            #Turning again the window dimensions to 1000,700   
            screen = pygame.display.set_mode((1000, 700))
            # Clears the screen with a very dark blue (0, 0, 20)
            screen_color = (0, 0, 20)
            screen.fill(screen_color)
            #Load the image of human win in given coordinates
            screen.blit(humanwin, (750,40))
        #If dont, just continue the game loop    
        else :
            pass
                    
    def getValidMoves(self):
        #Start the list of moves empty
        moves = []
        #Setting to the variable Moves all the possivle moves function 
        moves = self.getAllPossibleMoves()
        #check if the human has no more possible moves
        if not moves and self.humanToMove:
            #Turning the zombie win to true
            self.zombieWin = True
            #Turning again the window dimensions to 1000,700 
            screen = pygame.display.set_mode((1000, 700))
            # Clears the screen with a very dark blue (0, 0, 20)
            screen_color = (0, 0, 20)
            screen.fill(screen_color)
            #Load the image of zombie win in given coordinates
            screen.blit(zombiewin, (750,40))
        #return the vali moves    
        return moves

    #Get all moves by turns
    def getAllPossibleMoves(self):
        #Start the list of moves empty
        moves = []
        #Check if the move is inside the board rows
        for r in range(len(self.board)):
            #Check if the move is inside the board columns
            for c in range(len(self.board[r])):
                #Switching between player and zombie turns
                turn = self.board[r][c]
                if(turn == "human" and self.humanToMove) or (turn == "zombie" and not self.humanToMove):
                    player = self.board[r][c][0] 
                    if player == "h":
                        self.humanMoves(r, c, moves)
                    elif player == "z":
                        self.zombieMoves(r, c, moves)
        return moves

    #Human movement    
    def humanMoves (self, r, c, moves):
        #Player movement directions
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) #4 diaganols
        #A cicle fot each direction available
        for i in range(4):
            #Setting the end of the columns and rows
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            #Check a valid move inside the board
            if 0 <= endRow < 8 and -1 <= endCol < 8:
                newMove = self.board[endRow][endCol]
                #Check if is an empty place to move
                if newMove == "--": 
                    #makes the movement to that square
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                #if its a zombie in the square just pass
                elif newMove[0] == "zombie":
                    pass
            #Check if the move is off board    
            else:
                break

    #Zombie Movement
    def zombieMoves (self, r, c, moves):
        #Zombie movement directions
        directions = ((1, -1), (1, 1)) #2 diaganols
        #A cicle fot each direction available
        for j in range(2):
            #Setting the end of the columns and rows
            endRow = r + directions[j][0]
            endCol = c + directions[j][1] 
            #Check a valid move inside the board
            if 0 <= endRow < 8 and -1 <= endCol < 8:
                newMove = self.board[endRow][endCol]
                #check if the square is empty
                if newMove == "--": 
                    #makes the movement to that square
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                #if its a human in the square just pass    
                elif newMove[0] == "human": # enemy piece valid
                    pass
            #Check if the move is off board        
            else:
                break
    
class Move():

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.gameover = False
        #Check a valid move inside the board
        if 0 <= self.startRow < 8 and 0 <= self.startCol < 8:
            self.playerMoved = board[self.startRow][self.startCol]
            
        #Check If the human reaches the row 0
        if self.playerMoved == "human" and self.endRow == 0:
            #if yes turn the game over to true 
            self.gameover = True
        #Set the valid moves into x coordinates    
        self.moveID = self.startRow* 1000 + self.startCol *100 +self.endRow*10 +self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False