import socket
import threading

# Connection data
HOST = socket.gethostbyname(socket.gethostname())
PORT = 60000
ADDRESS = (HOST, PORT)

# Encoding format
FORMAT = "utf-8"

# Command for leaving
DISCONNECT_COMMAND = "!DISCONNECT"

# User inputs nickname
nickname = input("Choose your nickname: ")

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def receive():
    """
    Handles receiving messages from the server.

    :param: none
    """
    while True:
        try:
            # Receive Message From Server
            # If "NICK" Send Nickname
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(nickname.encode(FORMAT))
            elif message == f"The nickname \"{nickname}\" is taken!":
                print(message)
                print("Your connection is now closed\n"
                      "Press enter to exit")
                client.close()
                break
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def send():
    """
    Handles sending messages to the server and
    disconnecting the user if they send the
    DISCONNECT_COMMAND.

    :param: none
    """
    while True:
        contents = input()
        message = f"{nickname}: {contents}"

        if DISCONNECT_COMMAND in contents:
            client.close()

        client.send(message.encode(FORMAT))


# Starting threads for sending and receiving
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()