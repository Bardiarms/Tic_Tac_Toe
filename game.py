from board import Board
from threading import Thread, Semaphore
from socket import socket
from time import sleep


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


    def add_to_waiting(self, sock: socket, dim: int):
        
        if (dim == 3):
            self.w3s.acquire()
            self.ready_semaphore.acquire()

            self.waiting3.append(sock)
            self.ready[sock] = 0
            if (len(self.waiting3) >= 2):
                self.create_match_3()

            self.ready_semaphore.release()
            self.w3s.release()        

        elif (dim == 4):
            self.w4s.acquire()
            self.ready_semaphore.acquire()

            self.waiting4.append(sock)
            self.ready[sock] = 0
            if (len(self.waiting4) >= 2):
                self.create_match_4()

            self.ready_semaphore.release()
            self.w4s.release()

        else:
            self.w5s.acquire()
            self.ready_semaphore.acquire()

            self.waiting5.append(sock)
            self.ready[sock] = 0
            if (len(self.waiting5) >= 2):
                self.create_match_5()

            self.ready_semaphore.release()
            self.w5s.release()
        
        return
    

    def create_match_3(self):
                
        board = Board(3)
        
        self.w3s.acquire()
        self.ready_semaphore.acquire()

        p1 = self.waiting3.pop(0)
        p2 = self.waiting3.pop(0)

        self.ready[p1] = 1
        self.ready[p2] = 1


        self.ready_semaphore.release()
        self.w3s.release()


    def create_match_4(self):

        board = Board(4)
            
        self.w4s.acquire()
        self.ready_semaphore.acquire()

        p1 = self.waiting4.pop(0)
        p2 = self.waiting4.pop(0)

        self.ready[p1] = 1
        self.ready[p2] = 1
       

        self.ready_semaphore.release()
        self.w4s.release()



    def create_match_5(self):
    
        board = Board(5)
            
        self.w5s.acquire()
        self.ready_semaphore.acquire()

        p1 = self.waiting5.pop(0)
        p2 = self.waiting5.pop(0)
        
        self.ready[p1] = 1
        self.ready[p2] = 1
        
        self.ready_semaphore.release()
        self.w5s.release()
    

    
    def ready_to_play(self, sock: socket):

        while(True):
            if (self.ready[sock] == 1):
                return 1
            sleep(3)
            


    #create a function which checks if client can start a game