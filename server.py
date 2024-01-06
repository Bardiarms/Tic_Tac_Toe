from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread, Lock



HOST = "127.0.0.1"
PORT = 10001

lock = Lock()


def serve_client(lock: Lock):    # target for thread object
    pass



sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST,PORT))
sock.listen(15)


while (True):
    
    c, addr = sock.accept()