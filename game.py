from board import Board
from threading import Thread, Semaphore
from socket import socket
from time import sleep
import numpy as np


class Game():

    def __init__(self):
        self.waiting3 = list()
        self.waiting4 = list()
        self.waiting5 = list()

        self.w3s = Semaphore()
        self.w4s = Semaphore()
        self.w5s = Semaphore()

        self.ready = dict()
        self.ready_semaphore = Semaphore()


            

   
    def make_match3(self, sock: socket):
        """"""

        self.w3s.acquire()
        
        if (len(self.waiting3) == 0):   # No other player is waiting for a match
            board = Board(3)
            board.p1 = sock
            board.players[0] = 1
            self.waiting3.append(board)
            self.w3s.release()
            
            while (True):
                msg = "Waiting for an opponent... "
                sock.send(msg.encode())
                if (board.players[1] != 0):
                    msg = "Match started! \nYou are (x)"
                    sock.send(msg.encode())
                    break
                sleep(3)

            # game starts
            board.show_board()
            
            while (True):
                
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit(0)
                
                if (board.turn == 0):
                    
                    sock.send("Do your move.".encode())

                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<r<board.dim) and (0<c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                        
                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "x"
                    print(board.game_board)
                    if (board.row_win("x") or board.column_win("x") or board.diag_win("x")):
                        sock.send("You won the game!! ".encode())
                        board.p2.send("Your opponent won the game!! ".encode())
                        board.end_game = True

                    board.board_semaphore.release()   
                    board.show_board()     
                    board.turn = 1
                sleep(1.5)



        else:                           # There is already a player who is waiting for an opponent.
            
            board = self.waiting3.pop()
            self.w3s.release()
            board.p2 = sock
            board.players[1] = 1
            sock.send("Match started! \n You are (o).".encode())

            while (True):
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit()
                
                if (board.turn == 1):
                    sock.send("Do your move. ".encode())
                    
                   
                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<r<board.dim) and (0<c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                    
                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "o"
                    
                    if (board.row_win("o") or board.column_win("o") or board.diag_win("o")):
                        sock.send("You won the game!! ".encode())
                        board.p1.send("Your opponent won the game!! ".encode())
                        board.end_game = True
                    
                    board.board_semaphore.release()
                    board.show_board()
                    board.turn = 0
                sleep(1.5)




    def make_match4(self, sock: socket):
    
        self.w4s.acquire()
        
        if (len(self.waiting4) == 0):   # No other player is waiting for a match
            board = Board(4)
            board.p1 = sock
            board.players[0] = 1
            self.waiting4.append(board)
            self.w4s.release()
            
            while (True):
                msg = "Waiting for an opponent... "
                sock.send(msg.encode())
                if (board.players[1] != 0):
                    msg = "Match started! \nYou are (x)"
                    sock.send(msg.encode())
                    break
                sleep(3)

            # Game begins
            board.show_board()
            
            while (True):
                
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit(0)
                
                if (board.turn == 0):
                    
                    sock.send("Do your move.".encode())

                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<r<board.dim) and (0<c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                      
                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "x"
                    print(board.game_board)
                    if (board.row_win("x") or board.column_win("x") or board.diag_win("x")):
                        sock.send("You won the game!! ".encode())
                        board.p2.send("Your opponent won the game!! ".encode())
                        board.end_game = True

                    board.board_semaphore.release()   
                    board.show_board()     
                    board.turn = 1
                sleep(1.5)



        else:                           # There is already a player who is waiting for an opponent.
            
            board = self.waiting4.pop()
            self.w4s.release()
            board.p2 = sock
            board.players[1] = 1
            sock.send("Match started! \nYou are (o).".encode())

            while (True):
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit()
                
                if (board.turn == 1):
                    sock.send("Do your move. ".encode())

                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<r<board.dim) and (0<c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())

                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "o"
                    
                    if (board.row_win("o") or board.column_win("o") or board.diag_win("o")):
                        sock.send("You won the game!! ".encode())
                        board.p1.send("Your opponent won the game!! ".encode())
                        board.end_game = True
                    
                    board.board_semaphore.release()
                    board.show_board()
                    board.turn = 0
                sleep(1.5)



    def make_match5(self, sock: socket):
        
        self.w5s.acquire()
        
        if (len(self.waiting5) == 0):   # No other player is waiting for a match
            board = Board(5)
            board.p1 = sock
            board.players[0] = 1
            self.waiting5.append(board)
            self.w5s.release()
            
            while (True):
                msg = "Waiting for an opponent... "
                sock.send(msg.encode())
                if (board.players[1] != 0):
                    msg = "Match started! \nYou are (x)"
                    sock.send(msg.encode())
                    break
                sleep(3)

            # Game begins.
            board.show_board()
            
            while (True):
                
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit(0)
                
                if (board.turn == 0):
                    
                    sock.send("Do your move.".encode())

                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<r<board.dim) and (0<c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                        
                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "x"
                    print(board.game_board)
                    if (board.row_win("x") or board.column_win("x") or board.diag_win("x")):
                        sock.send("You won the game!! ".encode())
                        board.p2.send("Your opponent won the game!! ".encode())
                        board.end_game = True

                    board.board_semaphore.release()   
                    board.show_board()     
                    board.turn = 1
                sleep(1.5)



        else:                           # There is already a player who is waiting for an opponent.
            
            board = self.waiting5.pop()
            self.w5s.release()
            board.p2 = sock
            board.players[1] = 1
            sock.send("Match started! \nYou are (o).".encode())

            while (True):
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit()
                
                if (board.turn == 1):
                    sock.send("Do your move. ".encode())
            
                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<r<board.dim) and (0<c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())

                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "o"
                    
                    if (board.row_win("o") or board.column_win("o") or board.diag_win("o")):
                        sock.send("You won the game!! ".encode())
                        board.p1.send("Your opponent won the game!! ".encode())
                        board.end_game = True
                    
                    board.board_semaphore.release()
                    board.show_board()
                    board.turn = 0
                sleep(1.5)





def parse(string: str, dim: int) -> tuple:

    s0 = int(string[0])
    s1 = int(string[1])

    if ((-1<s0<dim) and (-1<s1<dim)):
        return (s0, s1)
    else: return (-1, -1)


def check_valid(arr: np.array, row: int, col: int) -> bool:
    
    if (arr[row][col] == "-"):
        return True
    return False