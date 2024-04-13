# server.py
import socket
from main import Main


def server_side():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9988)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("Waiting for a connection...")

    while True:
        client_socket, client_address = server_socket.accept()

        try:
            print("Connection from", client_address)
            player_name = client_socket.recv(1024).decode()
            print("Received player name:", player_name)

            Main(player_name)

        finally:
            client_socket.close()


server_side()
