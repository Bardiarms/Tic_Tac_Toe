from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread




HOST = "127.0.0.1"
PORT = 9001


sock = socket(AF_INET, SOCK_STREAM)             # Connecting client to server
sock.connect((HOST, PORT))


def send_thread(socket: socket):                # Target for the thread object whitch is responsible for sending messages 
    while (True):
        msg = input()
        socket.send(msg.encode())


def recv_thread(socket: socket):                # Target for the thread object whitch is responsible for recieving messages
    while (True):
        res = socket.recv(1024).decode()
        print(res)
        if (res == "End of the game."):
            exit(0)




s_thread = Thread(target=send_thread, args=(sock,))
s_thread.start()

r_thread = Thread(target=recv_thread, args=(sock,))
r_thread.start()