import socket
from threading import Thread

host = '127.0.0.1'
port = 8080
clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

def handle_clients(connection, address):
    name = connection.recv(1024).decode()
    welcome = "Welcome " + name + ". You can type #quite if you event want to leave the Chat Room"
    connection.send(bytes(welcome, "UTF8"))
    msg = name + " Has recently joined the Chat Room"
    broadcast(bytes(msg, "UTF8"))
    clients[connection] = name

    while True:
        msg = connection.recv(1024)
        if msg != bytes("#quite", "UTF8"):
            broadcast(msg, name + ":")
        else:
            connection.send(bytes("#quite", "UTF8"))
            connection.close()
            del clients[connection]
            broadcast(bytes(name + " Has left the Chat Room", "UTF8"))

def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "UTF8") + msg)

def accept_clients_connections():
    while True:
        client_connection, client_address = sock.accept()
        print(client_address, "Has connected")
        client_connection.send(" Welcome to the Chat Room, Please type your name to continue: ".encode("UTF8"))
        addresses[client_connection] = client_address

        Thread(target=handle_clients, args=(client_connection, client_address)).start()


if __name__ == "__main__":
    sock.listen(5)
    print("The server is running and is listening to clients request")
    t1 = Thread(target=accept_clients_connections)
    t1.start()
    t1.join()
