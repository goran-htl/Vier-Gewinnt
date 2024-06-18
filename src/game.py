#Goran Nastasijevic
#Furkan Gueyen

from board import Board  # Import der Board-Klasse aus board.py
from player import Player  # Import der Player-Klasse aus player.py

class ConnectFourCLI:
    def __init__(self):
        self.board = Board()  # Initialisiert das Spielbrett
        self.players = [Player("Spieler 1", 'X'), Player("Spieler 2", 'O')]  # Erstellt die Spieler mit ihren Namen und Spielsteinen
        self.current_player = 0  # Index des aktuellen Spielers (0 für Spieler 1)

    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2  # Wechselt zum nächsten Spieler

    def play(self):
        print("Willkommen zu Vier Gewinnt!")  # Begrüßungsnachricht auf Deutsch
        print(self.board)  # Zeigt das Spielbrett an

        while True:
            player = self.players[self.current_player]  # Aktueller Spieler
            col = int(input(f"{player.name} ({player.piece}), wähle eine Spalte (0-{self.board.cols-1}): "))  # Spieler wählt eine Spalte

            if col < 0 or col >= self.board.cols or not self.board.drop_piece(col, player.piece):
                print("Ungültiger Zug. Bitte versuche es erneut.")  # Fehlermeldung für ungültige Züge
                continue

            print(self.board)  # Zeigt das Spielbrett nach einem Zug an

            if self.board.is_winner(player.piece):
                print(f"Herzlichen Glückwunsch {player.name}, du hast gewonnen!")  # Gewinnnachricht für den Spieler
                break

            if self.board.is_full():
                print("Unentschieden! Das Spielfeld ist voll.")  # Nachricht für ein Unentschieden
                break

            self.switch_player()  # Wechselt zum nächsten Spieler

if __name__ == "__main__":
    game = ConnectFourCLI()  # Erstellt eine Instanz des Spiels
    game.play()  # Startet das Spiel

