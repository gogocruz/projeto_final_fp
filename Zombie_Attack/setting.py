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
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        print(self.startRow,self.startCol)

 
    def makeMove(self,player, row, col):
        self.board[player.row][player.col], self.board[row][col] = self.board[row][col] , self.board[player.row][player.col]
        player.move(row, col)

    def get_player(self, row, col):
        return self.board[row][col]

   
            


