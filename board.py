from threading import Semaphore




class Board():

    def __init__(self, dim: int):

        self.dim = dim
        self.game_board = [[0]*dim]*dim 
        self.board_semaphore = Semaphore()