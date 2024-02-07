from threading import Semaphore
from socket import socket
import numpy as np




class Board():

    def __init__(self, dim: int):

        self.dim = dim
        self.game_board = np.array([['-']*dim]*dim) 
        self.board_semaphore = Semaphore()
        self.p1 = socket()
        self.p2 = socket()
        self.players = [0]*2
        self.turn = 0 
        self.end_game = False


    def check_end(self) -> bool:
        
        if (self.end_game):
            
            return True
        
        return False


    def show_board(self):
        tmp = str()
        for i in range(self.dim):
            tmp = tmp + "\n"
            for j in range(self.dim):
                tmp = tmp + self.game_board[i][j] + " "
        
        self.p1.send(tmp.encode())
        self.p2.send(tmp.encode())
        

    def column_win(self, xo: str) -> bool:
    
        for i in range(self.dim):
            if (i+2 < self.dim):
                for j in range(self.dim):
                    if (xo==self.game_board[i][j]==self.game_board[i+1][j]==self.game_board[i+2][j]):
                        return True
        
        return False

    
    def row_win(self, xo: str) -> bool:
    
        for i in range(self.dim):
            for j in range(self.dim):
                if (j+2 < self.dim):
                    if (xo==self.game_board[i][j]==self.game_board[i][j+1]==self.game_board[i][j+2]):
                        return True
        
        return False
    

    def diag_win(self, xo: str) -> bool:

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