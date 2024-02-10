from board import Board
from threading import Thread, Semaphore
from socket import socket
from time import sleep
import numpy as np




    
class Game():
    """"""
    def __init__(self):
        self.waiting3 = list()              # Waiting lists carry game objects which are waiting for 
        self.waiting4 = list()
        self.waiting5 = list()

        self.w3s = Semaphore()              # Semaphores for each waiting list
        self.w4s = Semaphore()
        self.w5s = Semaphore()

        #self.ready = dict()
        #self.ready_semaphore = Semaphore()


            

   
    def make_match3(self, sock: socket):
        """This module is responsible for connecting a client to another one.
        If no ther were no other player waiting for a 3X3 match, it creates a match and waits for another
        player. If there was already a player waiting for another player,
        it connects the client to that player."""

        self.w3s.acquire()
        
        if (len(self.waiting3) == 0):   # No other player is waiting for a match
            board = Board(3)        # Creating a game board
            board.p1 = sock
            board.players[0] = 1
            self.waiting3.append(board)    # Adding the board to waiting list
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
                
                if (board.turn == 0):           # Client is the one who made the match (no other players were waiting).
                                                # so it should play whenever turn=0.
                    sock.send("Do your move.".encode())

                    while(True):
                        move = sock.recv(1024).decode() # Waiting for clients response
                        r, c = parse(move, board.dim)   # parsing the response.
                        #print()
                        if (check_valid(board.game_board, r, c) and (0<=r<board.dim) and (0<=c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                        
                    board.board_semaphore.acquire() # If everythig was alright, it is time to modify the board.
                    board.game_board[r][c] = "x"
                    print(board.game_board)
                    if (board.row_win("x") or board.column_win("x") or board.diag_win("x")):    # Checking if player won the game after this move
                        sock.send("You won the game!! ".encode())
                        board.p2.send("Your opponent won the game!! ".encode())
                        board.end_game = True

                    board.board_semaphore.release()   
                    board.show_board()     
                    board.turn = 1
                sleep(1.5) 



        else:                           # There is already a player who is waiting for an opponent.
            
            board = self.waiting3.pop()     # Popping the game board from waiting list.
            self.w3s.release()
            board.p2 = sock
            board.players[1] = 1
            sock.send("Match started! \n You are (o).".encode())

            while (True):
                if (board.check_end()):
                    sock.send("End of the game.".encode())
                    exit()
                
                if (board.turn == 1):                       # Client is the one who was added to a match.
                                                            # So it should play whenever turn=1.
                    sock.send("Do your move. ".encode())
                    
                   
                    while(True):
                        move = sock.recv(1024).decode()
                        r, c = parse(move, board.dim)
                        print(r, c)
                        if (check_valid(board.game_board, r, c) and (0<=r<board.dim) and (0<=c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                    
                    board.board_semaphore.acquire()         # Waiting for clients response
                    board.game_board[r][c] = "o"            # parsing the response.
                    
                    if (board.row_win("o") or board.column_win("o") or board.diag_win("o")):
                        sock.send("You won the game!! ".encode())
                        board.p1.send("Your opponent won the game!! ".encode())
                        board.end_game = True
                    
                    board.board_semaphore.release()
                    board.show_board()
                    board.turn = 0
                sleep(1.5)




    def make_match4(self, sock: socket):

        """This module is responsible for connecting a client to another one.
        If no ther were no other player waiting for a 4X4 match, it creates a match and waits for another
        player. If there was already a player waiting for another player,
        it connects the client to that player. (Codes in this section are the same as the
        previous section(3X3). Difference are just for the size of the board)"""
    
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
                        if (check_valid(board.game_board, r, c) and (0<=r<board.dim) and (0<=c<board.dim)):
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
                        if (check_valid(board.game_board, r, c) and (0<=r<board.dim) and (0<=c<board.dim)):
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
        
        """This module is responsible for connecting a client to another one.
        If no ther were no other player waiting for a 5X5 match, it creates a match and waits for another
        player. If there was already a player waiting for another player,
        it connects the client to that player.(Codes in this section are the same as the
        previous sections(3X3 and 4X4). Difference are just for the size of the board)"""

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
                        if (check_valid(board.game_board, r, c) and (0<=r<board.dim) and (0<=c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())
                        
                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "x"
                    print(board.game_board)
                    if (board.row_win_4("x") or board.column_win_4("x") or board.diag_win_4("x")):
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
                        if (check_valid(board.game_board, r, c) and (0<=r<board.dim) and (0<=c<board.dim)):
                            break
                        sock.send("Invalid input! try again: ".encode())

                    board.board_semaphore.acquire()
                    board.game_board[r][c] = "o"
                    
                    if (board.row_win_4("o") or board.column_win_4("o") or board.diag_win_4("o")):
                        sock.send("You won the game!! ".encode())
                        board.p1.send("Your opponent won the game!! ".encode())
                        board.end_game = True
                    
                    board.board_semaphore.release()
                    board.show_board()
                    board.turn = 0
                sleep(1.5)





def parse(string: str, dim: int) -> tuple:          # parses the client's input for rows and columns.

    s0 = int(string[0])
    s1 = int(string[1])

    if ((-1<s0<dim) and (-1<s1<dim)):
        return (s0, s1)
    else: return (-1, -1)


def check_valid(arr: np.array, row: int, col: int) -> bool:  # Checks if the given input in the chart is empty.
    
    if (arr[row][col] == "-"):
        return True
    return False