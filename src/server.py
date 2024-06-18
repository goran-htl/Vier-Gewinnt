import socket
import threading
from board import Board
from player import Player

class ConnectFourServer:
    def __init__(self, host='localhost', port=65432):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        self.players = []
        self.board = Board()
        self.current_player = 0
        print("Server gestartet. Warte auf Verbindungen...")

    def handle_client(self, conn, addr, player):
        print(f"Spieler {player.piece} verbunden: {addr}")
        conn.sendall(f"Du bist Spieler {player.piece}".encode('utf-8'))
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                col = int(data.decode('utf-8'))
                if self.board.drop_piece(col, player.piece):
                    if self.board.is_winner(player.piece):
                        conn.sendall("GEWINNER".encode('utf-8'))
                        break
                    elif self.board.is_full():
                        conn.sendall("UNENTSCHIEDEN".encode('utf-8'))
                        break
                    else:
                        self.current_player = (self.current_player + 1) % 2
                        self.broadcast_board()
                else:
                    conn.sendall("UNGÜLTIGER ZUG".encode('utf-8'))
            except Exception as e:
                print(f"Fehler: {e}")
                break
        conn.close()

    def broadcast_board(self):
        board_str = str(self.board).encode('utf-8')
        for player in self.players:
            player.conn.sendall(board_str)

    def start(self):
        while len(self.players) < 2:
            conn, addr = self.server.accept()
            player = Player(f"Spieler {len(self.players) + 1}", 'X' if len(self.players) == 0 else 'O')
            player.conn = conn
            self.players.append(player)
            threading.Thread(target=self.handle_client, args=(conn, addr, player)).start()
        print("Beide Spieler sind verbunden. Spiel startet.")

if __name__ == "__main__":
    server = ConnectFourServer()
    server.start()
