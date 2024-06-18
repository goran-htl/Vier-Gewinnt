import socket
import threading
from board import Board

clients = []
nicknames = []
colors = ['X', 'O']
board = Board()

def sende_an_alle(nachricht):
    for client in clients:
        client.send(nachricht)

def handle(client):
    farbe = colors[len(clients) % 2]  # Weisen Sie 'X' dem ersten Spieler und 'O' dem zweiten zu
    while True:
        try:
            nachricht = client.recv(1024).decode('utf-8')
            spalte = int(nachricht)
            if board.drop_piece(spalte, farbe):
                sende_an_alle(f"{spalte}".encode('utf-8'))
                if board.check_winner(farbe):
                    sende_an_alle(f"{farbe} gewinnt!".encode('utf-8'))
                    board.reset()
            else:
                client.send("Ungültiger Zug".encode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            sende_an_alle(f'{nickname} hat das Spiel verlassen!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def empfange():
    while True:
        client, address = server.accept()
        print(f"Verbunden mit {str(address)}")

        client.send('VERBUNDEN'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname ist {nickname}")
        sende_an_alle(f"{nickname} hat das Spiel betreten!".encode('utf-8'))
        client.send('Mit dem Server verbunden!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen()

print("Server hört zu...")
empfange()
