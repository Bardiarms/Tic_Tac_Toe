from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread, Semaphore
from board import Board
from game import Game
from server_functions import *




HOST = "127.0.0.1"
PORT = 9001





game = Game()



sock = socket(AF_INET, SOCK_STREAM)         # Creating server's socket 
sock.bind((HOST,PORT))
sock.listen(15)

print("Server is Ready")

while (True):
            # Accepting clients and passing each of them to a different thread. 
    c, addr = sock.accept()
    t = Thread(target=serve_client, args=(c, game))
    t.start()