from board import Board
from threading import Thread, Semaphore
from socket import socket


class Game():

    def __init__(self):
        self.waiting3 = list()
        self.waiting4 = list()
        self.waiting5 = list()

        self.w3s = Semaphore()
        self.w4s = Semaphore()
        self.w5s = Semaphore()


    def add_to_waiting(self, sock: socket, dim: int):
        
        if (dim == 3):
            self.w3s.acquire()
    
            self.waiting3.append(sock)
            if (len(self.waiting3 >= 2)):
                self.create_match_3

            self.w3s.release()        

        elif (dim == 4):
            self.w4s.acquire()

            self.waiting4.append(sock)
            if (len(self.waiting4 >= 2)):
                self.create_match_4


            self.w4s.release()

        else:
            self.w5s.acquire()

            self.waiting5.append(sock)
            if (len(self.waiting4 >= 2)):
                self.create_match_4


            self.w5s.release()
        
        return
    

    def create_match_3(self):
                
        board = Board(3)
            


        self.w3s.acquire()
        self.waiting3.pop(0)
        self.w3s.release()


    def create_match_4(self):

        board = Board(4)
            


        self.w4s.acquire()
        self.waiting4.pop(0)
        self.w4s.release()



    def create_match_5(self):
    
        board = Board(5)
            


        self.w5s.acquire()
        self.waiting5.pop(0)
        self.w5s.release()
    

    def ready_to_play(self, sock: socket):

        pass


    #create a function which checks if client can start a game