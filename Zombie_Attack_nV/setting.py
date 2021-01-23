import pygame 

humanwin = pygame.image.load("images/humanwins.png")
zombiewin = pygame.image.load("images/zombieswin.png")

class GameState():
    def __init__(self):
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
        self.humanToMove = True
        self.humanWin = False
        self.zombieWin = False
        
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.playerMoved
        self.humanToMove = not self.humanToMove
        if move.gameover:
            self.humanWin = True
            screen = pygame.display.set_mode((1000, 700))
            screen_color = (0, 0, 20)
            screen.fill(screen_color)
            screen.blit(humanwin, (750,40))
        else :
            pass
                    
    def getValidMoves(self):
        moves = []
        moves = self.getAllPossibleMoves()
        if not moves and self.humanToMove:
            self.zombieWin = True
            screen = pygame.display.set_mode((1000, 700))
            screen_color = (0, 0, 20)
            screen.fill(screen_color)
            screen.blit(zombiewin, (750,40))
        return moves

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c]
                if(turn =="human" and self.humanToMove) or (turn == "zombie" and not self.humanToMove):
                    player = self.board[r][c][0]
                    if player == "h":
                        self.playerMoves(r, c, moves)
                    elif player == "z":
                        self.enemyMoves(r, c, moves)
        return moves
        
    def playerMoves (self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) #4 diaganols
        enemy = "z" if self.humanToMove else "h" #turns
        for i in range(4):
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            if 0 <= endRow < 8 and -1 <= endCol < 8:
                endPlayer = self.board[endRow][endCol]
                if endPlayer == "--": # empty space valid
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                elif endPlayer[0] == enemy: # enemy 
                    pass
            else: # off board
                break

    def enemyMoves (self, r, c, moves):
        directions = ((1, -1), (1, 1)) #2 diaganols
        player = "h" if not self.humanToMove else "z"
        for j in range(2):
            endRow = r + directions[j][0]
            endCol = c + directions[j][1] 
            if 0 <= endRow < 8 and -1 <= endCol < 8:
                endPlayer = self.board[endRow][endCol]
                if endPlayer == "--": # empty space valid
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                elif endPlayer[0] == player: # enemy piece valid
                    pass
            else:
                break
    
class Move():

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.gameover = False

        if 0 <= self.startRow < 8 and 0 <= self.startCol < 8:
            self.playerMoved = board[self.startRow][self.startCol]

        if self.playerMoved == "human" and self.endRow == 0:
            self.gameover = True
            
        self.moveID = self.startRow* 1000 + self.startCol *100 +self.endRow*10 +self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False