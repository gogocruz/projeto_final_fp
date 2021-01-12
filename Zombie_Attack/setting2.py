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

            

class Move():

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        print(self.startRow,self.startCol)
        self.playerMoved = board[self.startRow][self.startCol] 
        self.playerCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow* 1000 + self.startCol *100 +self.endRow*10 +self.endCol

    '''
    Overriding the equal method
    '''

#    def __eq__(self, other):
#        if isinstance(other, Move):
#            return self.moveID == other.moveID
#        return False


def getValidMoves(self):
    return self.getAllPossibleMoves()


#def getAllPossibleMoves(self):
#    moves = []
#    for r in range (len(self.board)):
#        for c in range(le(self.board[r])):
            
