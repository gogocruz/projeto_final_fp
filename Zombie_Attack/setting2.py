import pygame 

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
            ["human","--","--","--","--","--","--","--"]
        ]
        self.humanToMove= True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startCol] ="--"
        self.board[move.endRow][move.endCol] = move.playerMoved
        self.moveLog.append(move)
        self.humanToMove = not self.humanToMove

    def getValidMoves(self):
        return self.getAllPossibleMoves()

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if(turn =="h" and self.humanToMove) or (turn == "z" and not self.humanToMove):
                    player = self.board[r][c][1]
                    if player == "u":
                        self.playerMoves(r, c, moves)
                    elif player == "o":
                        self.enemyMoves(r, c, moves)
        return moves

    def playerMoves (self, r, c, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) #4 diaganols
        enemy = "z" if self.humanToMove else "h" #turns
        for i in range(4):
            endRow = r + directions[i][0]
            endCol = c + directions[i][1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPlayer = self.board[endRow][endCol]
                if endPlayer == "--": # empty space valid
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                elif endPlayer[0] == enemy: # enemy 
                    break
                else: # off board
                    break

    def enemyMoves (self, r, c, moves):
        directions = ((1, -1), (1, 1)) #2 diaganols
        player = "h" if not self.humanToMove else "z"
        for j in range(2):
            endRow = r + directions[j][0]
            endCol = c + directions[j][1] 
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPlayer = self.board[endRow][endCol]
                if endPlayer == "--": # empty space valid
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                elif endPlayer[0] == player: # enemy piece valid
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                    break
                    

class Move():


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        if 0 <= self.startRow < 8 and 0 <= self.startCol < 8:
            self.playerMoved = board[self.startRow][self.startCol]
        if 0 <= self.endRow < 8 and 0 <= self.endCol < 8:
            self.playerCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow* 1000 + self.startCol *100 +self.endRow*10 +self.endCol

    
                    
    '''
    Overriding the equal method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False