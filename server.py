from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread, Semaphore
from board import Board
from game import Game
from server_functions import *




HOST = "127.0.0.1"
PORT = 10001




lock_for_game = Semaphore()
game = Game()


t1 = Thread(target=game.create_match_3)
t2 = Thread(target=game.create_match_4)
t3 = Thread(target=game.create_match_5)
t1.start()
t2.start()
t3.start()


sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(15)


while (True):
    
    c, addr = sock.accept()
    t = Thread(target=serve_client, args=(lock_for_game, c, game))