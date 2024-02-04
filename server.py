from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread, Semaphore
from board import Board
from game import Game
from server_functions import *




HOST = "127.0.0.1"
PORT = 10001




lock_for_game = Semaphore()
game = Game()



sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(15)


while (True):
    
    c, addr = sock.accept()
    t = Thread(target=serve_client, args=(lock_for_game, c, game))
    t.start()