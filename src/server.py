# server.py

import socket
import threading
from board import Board

clients = []
nicknames = []
colors = ['X', 'O']
board = Board((6, 7))  # Initialisiere das Board mit der richtigen Größe
aktueller_spieler_index = 0  # Variable, um den aktuellen Spieler zu verfolgen

def sende_an_alle(nachricht):
    print(f"Sending to all: {nachricht}")  # Debugging-Ausgabe
    for client in clients:
        client.send(nachricht.encode('utf-8'))

def handle(client, color):
    global aktueller_spieler_index
    while True:
        try:
            nachricht = client.recv(1024).decode('utf-8')
            print(f"Received message from client: {nachricht}")  # Debugging-Ausgabe
            if nachricht.startswith('SPALTE:'):
                spalte = int(nachricht.split(':')[1])
                if clients[aktueller_spieler_index] == client and board.drop_piece(spalte, color):
                    sende_an_alle(f"SPALTE:{spalte}:{color}")
                    if board.check_winner(color):
                        sende_an_alle(f"GEWINNER:{color}")
                        board.reset()
                    else:
                        aktueller_spieler_index = (aktueller_spieler_index + 1) % len(clients)
                        clients[aktueller_spieler_index].send("DEIN ZUG".encode('utf-8'))
                else:
                    client.send("Ungültiger Zug".encode('utf-8'))
            else:
                client.send("Ungültige Nachricht".encode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            sende_an_alle(f'{nickname} hat das Spiel verlassen!')
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

        color = colors[len(clients) % 2]  # Weisen Sie 'X' dem ersten Spieler und 'O' dem zweiten zu
        client.send(f'FARBE:{color}'.encode('utf-8'))

        print(f"Nickname ist {nickname} und Farbe ist {color}")
        sende_an_alle(f"{nickname} hat das Spiel betreten!")
        client.send('Mit dem Server verbunden!'.encode('utf-8'))

        if len(clients) == 2:
            clients[aktueller_spieler_index].send("DEIN ZUG".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client, color))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5555))
server.listen()

print("Server hört zu...")
empfange()
