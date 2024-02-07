from socket import socket
from game import Game
from threading import Semaphore







def choose_board(sock: socket) -> int:
    
    msg = "Enter 3 for 3x3, 4 for 4x4 and 5 for 5x5 board: "
    sock.send(msg.encode())
    while (True):
        res = int(sock.recv(1024).decode())
        if (res==3 or res==4 or res==5):
            return res
        else:                                   # remember to set an exit option
            print("Wrong input! try again: ")



def serve_client(sock: socket, game: Game):  
    """Target for thread object. Each client is assigned to one 
    instance of this method.\n Handles clients request"""  

    msg = "Welcome to the Tic-Tac-Toe game!"
    sock.send(msg.encode())

    res = choose_board(sock)

    if (res == 3):
        game.make_match3(sock)
    
    elif (res == 4):
        game.make_match4(sock)

    else:
        game.make_match5(sock)
    

   
    
    