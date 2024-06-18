import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)

    print("Server gestartet und wartet auf Verbindungen...")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Verbindung von {client_address}")

        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()

