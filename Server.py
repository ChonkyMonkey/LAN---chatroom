import socket
import threading

# Connection data
HOST = socket.gethostbyname(socket.gethostname())
PORT = 60000
ADDRESS = (HOST, PORT)

# Encoding format
FORMAT = "utf-8"

# Starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()

# Lists for clients and their respective nicknames
clients = []
nicknames = []


def broadcast(message):
    """
    Handles sending messages to all other clients

    :param message: messages from either server or client
    :return: none
    """
    for client in clients:
        client.send(message)
    return


def remove_clients(client):
    """
    Handles the removal of clients

    :param client
    :return:
    """
    index = clients.index(client)
    clients.remove(client)
    client.close()
    nickname = nicknames[index]
    broadcast(f"{nickname} has left the chat!".encode(FORMAT))
    print(f"{nickname} has disconnected")
    nicknames.remove(nickname)
    return


def handle_client(client):
    """
    Handles messages from the client,
    makes calls to either broadcast or remove_clients

    :param client:  the user joining the server
    :return: none
    """
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            remove_clients(client)
            break


def receive():
    """
    Handles receiving messages from clients

    :param: none
    :return: none
    """
    while True:
        # Accepts connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request and stores nicknames
        client.send("NICK".encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)

        # Only proceeds if nicknames are unique
        if len(nicknames) == len(set(nicknames)):
            clients.append(client)

            # Print and broadcast nickname
            print(f"Nickname of client is {nickname}")
            broadcast(f"{nickname} joined the chat!".encode(FORMAT))
            client.send("Connected to server!".encode(FORMAT))

        # Initiates a thread for client
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
            return
        else:
            # Removes nickname from list of nicknames
            nicknames.pop()
            client.send(f"The nickname \"{nickname}\" is taken!".encode(FORMAT))
            print(f"Disconnected with {str(address)} (duplicate nickname)")
            return


# Starts the server
print("Server is starting")
receive()
