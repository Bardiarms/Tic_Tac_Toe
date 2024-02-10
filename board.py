from threading import Semaphore
from socket import socket
import numpy as np




class Board():

    """This is an object representing a 1v1 tic-tac-toe game"""


    def __init__(self, dim: int):

        self.dim = dim      # 3 for 3X3, 4 for 4X4 and 5 for 5X5 game.
        self.game_board = np.array([['-']*dim]*dim)         # 2D array represanting game board
        self.board_semaphore = Semaphore()      # Semaphore for game_board
        self.p1 = socket()      # Storing players sockets
        self.p2 = socket()
        self.players = [0]*2    # turns 1 when players are added.
        self.turn = 0   # If turn=0, it's p1's turn and if turn=1, it's p2's turn.
        self.end_game = False   # Default is false. When a player wins, it changes to true.  


    def check_end(self) -> bool:        # Checks if one of the players has won the game.
        
        if (self.end_game):
            
            return True
        
        return False


    def show_board(self):               # Displays current status of the game board
        tmp = str()
        for i in range(self.dim):
            tmp = tmp + "\n"
            for j in range(self.dim):
                tmp = tmp + self.game_board[i][j] + " "
        
        self.p1.send(tmp.encode())
        self.p2.send(tmp.encode())
        

    def column_win(self, xo: str) -> bool:  

        """xo: X or O
        Checks if there are three consecutive (xo)s vertically."""
    
        for i in range(self.dim):
            if (i+2 < self.dim):
                for j in range(self.dim):
                    if (xo==self.game_board[i][j]==self.game_board[i+1][j]==self.game_board[i+2][j]):
                        return True
        
        return False

    
    def row_win(self, xo: str) -> bool:
    
        """xo: X or O
        Checks if there are three consecutive (xo)s horizontally."""

        for i in range(self.dim):
            for j in range(self.dim):
                if (j+2 < self.dim):
                    if (xo==self.game_board[i][j]==self.game_board[i][j+1]==self.game_board[i][j+2]):
                        return True
        
        return False
    

    def diag_win(self, xo: str) -> bool:

        """xo: X or O
        Checks if there are three consecutive (xo)s diagonally."""

        for i in range(self.dim):
            if (i+2 < self.dim):
                for j in range(self.dim):
                    if (j+2 < self.dim):
                        if (xo==self.game_board[i][j]==self.game_board[i+1][j+1]==self.game_board[i+2][j+2]):
                            return True
        
        for i in range(self.dim):
            if (i+2 < self.dim):
                for j in range(self.dim):
                    if (j-2 >= 0):
                        if (xo==self.game_board[i][j]==self.game_board[i+1][j-1]==self.game_board[i+2][j-2]):
                            return True
        
        return False
    
    def column_win_4(self, xo: str) -> bool:  

        """xo: X or O
        Checks if there are four consecutive (xo)s vertically."""
    
        for i in range(self.dim):
            if (i+3 < self.dim):
                for j in range(self.dim):
                    if (xo==self.game_board[i][j]==self.game_board[i+1][j]==self.game_board[i+2][j]==self.game_board[i+3][j]):
                        return True
        
        return False

    
    def row_win_4(self, xo: str) -> bool:
    
        """xo: X or O
        Checks if there are four consecutive (xo)s horizontally."""

        for i in range(self.dim):
            for j in range(self.dim):
                if (j+3 < self.dim):
                    if (xo==self.game_board[i][j]==self.game_board[i][j+1]==self.game_board[i][j+2]==self.game_board[i][j+3]):
                        return True
        
        return False
    

    def diag_win_4(self, xo: str) -> bool:

        """xo: X or O
        Checks if there are four consecutive (xo)s diagonally."""

        for i in range(self.dim):
            if (i+3 < self.dim):
                for j in range(self.dim):
                    if (j+3 < self.dim):
                        if (xo==self.game_board[i][j]==self.game_board[i+1][j+1]==self.game_board[i+2][j+2]==self.game_board[i+3][j+3]):
                            return True
        
        for i in range(self.dim):
            if (i+3 < self.dim):
                for j in range(self.dim):
                    if (j-3 >= 0):
                        if (xo==self.game_board[i][j]==self.game_board[i+1][j-1]==self.game_board[i+2][j-2]==self.game_board[i+2][j-2]):
                            return True
        
        return False