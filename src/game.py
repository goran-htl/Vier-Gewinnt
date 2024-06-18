from board import Board
from player import Player

class ConnectFourCLI:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", 'X'), Player("Player 2", 'O')]
        self.current_player = 0

    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2

    def play(self):
        print("Willkommen zu Vier Gewinnt!")
        print(self.board)

        while True:
            player = self.players[self.current_player]
            try:
                col = int(input(f"{player.name} ({player.piece}), wähle eine Spalte (0-{self.board.cols-1}): "))
                if col < 0 or col >= self.board.cols:
                    raise ValueError("Ungültige Spalte")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine gültige Spalte eingeben.")
                continue

            if self.board.drop_piece(col, player.piece):
                print(self.board)
                if self.board.is_winner(player.piece):
                    print(f"{player.name} hat gewonnen!")
                    break
                elif self.board.is_full():
                    print("Unentschieden! Das Spielfeld ist voll.")
                    break
                else:
                    self.switch_player()
            else:
                print("Diese Spalte ist voll. Bitte wähle eine andere Spalte.")

if __name__ == "__main__":
    game = ConnectFourCLI()
    game.play()
