#Furkan Gueyen
from board import Board  # Import der Board-Klasse aus board.py
from player import Player  # Import der Player-Klasse aus player.py

class ConnectFourCLI:
    def __init__(self):
        self.board = Board()  # Initialisierung eines neuen Spielbretts
        self.players = [Player("Spieler 1", 'X'), Player("Spieler 2", 'O')]
        self.current_player = 0  # Initialisierung des aktuellen Spielers (Index 0 für Spieler 1)

    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2  # Wechsel zum nächsten Spieler

    def play(self):
        print("Willkommen zu Vier Gewinnt!")
        print(self.board)  # Ausgabe des aktuellen Spielbretts

        while True:
            player = self.players[self.current_player]  # Aktueller Spieler basierend auf self.current_player
            try:
                col = int(input(f"{player.name} ({player.piece}), wähle eine Spalte (0-{self.board.cols-1}): "))  # Eingabe der Spielerspalte
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")  # Fehlermeldung für ungültige Eingaben (keine Zahl)
                continue

            if col < 0 or col >= self.board.cols or not self.board.drop_piece(col, player.piece):
                print("Ungültiger Zug. Bitte versuche es erneut.")  # Fehlermeldung für ungültige Spielzüge (Spalte außerhalb des Bereichs oder voll)
                continue

            print(self.board)  # Aktualisierte Ausgabe des Spielbretts nach einem gültigen Zug

            if self.board.is_winner(player.piece):
                print(f"Herzlichen Glückwunsch {player.name}, du hast gewonnen!")  # Gewinnnachricht für den Spieler
                break

            if self.board.is_full():
                print("Unentschieden! Das Spielfeld ist voll.")  # Nachricht für ein Unentschieden, wenn das Spielfeld voll ist
                break

            self.switch_player()  # Wechsel zum nächsten Spieler für den nächsten Zug

if __name__ == "__main__":
    game = ConnectFourCLI()  # Initialisierung eines neuen ConnectFourCLI-Spiels
    game.play()  # Starten des Spiels
