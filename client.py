import socket


def get_player_name():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9988))

        player_name = input("Enter your name: ")
        client_socket.send(player_name.encode())

        return player_name
    except ConnectionRefusedError:
        print("Server is not available.")
        # Don't return anything here


def main():
    username = get_player_name()
    return username


if __name__ == "__main__":
    main()
