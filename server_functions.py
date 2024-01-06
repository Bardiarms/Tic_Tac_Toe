from socket import socket
from game import Game
from threading import Semaphore







def choose_board(sock: socket):
    msg = "Enter 3 for 3x3, 4 for 4x4 and 5 for 5x5 board: "
    socket.send(msg.encode())
    while (True):
        res = int(sock.recv(1024).decode())
        if (res==3 or res==4 or res==5):
            return res
        else:                                   # remember to set an exit option
            print("Wrong input! try again: ")



def serve_client(semaphore: Semaphore, sock: socket, game: Game):    # target for thread object
    msg = "Welcome to the Tic-Tac-Toe game!"
    sock.send(msg.encode())

    res = choose_board(sock)

    game.add_to_waiting(sock, res)

    msg = "Waiting for an opponent..."
    sock.send(msg.encode())
