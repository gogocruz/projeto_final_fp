import  pygame


FPS = 60 #Base time for the game

# Name and logo of the game
pygame.display.set_caption('Zombie Attack') 
icon = pygame.image.load('img/human.png') 
pygame.display.set_icon(icon)


#Constants
WIDTH, HEIGHT = 1000, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = (50,50)

RED = (255,0,5)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)

#End of constants#

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
gboard = pygame.draw.rect(WIN, (255,255,0), (400,100, 500,500), 3)

#Board
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None

    def draw_squares(self, gboard):
        gboard.fill(BLACK)
        for row in range (ROWS):
            for col in range (row % 2, ROWS, 2):
                pygame.draw.rect(gboard, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
    def crate_board(self):
        pass
#End of Board #



def main():
    run = True
    clock = pygame.time.Clock() 
    board = Board()

    while run :
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_squares(gboard)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":  
    main()