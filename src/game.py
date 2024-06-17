from board import Board
from player import Player


class Game:
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
            col = int(input(f"{player.name} ({player.piece}), wähle eine Spalte (0-{self.board.cols-1}): "))

            if col < 0 or col >= self.board.cols or not self.board.drop_piece(col, player.piece):
                print("Ungültiger Zug. Bitte versuche es erneut.")
                continue

            print(self.board)

            if self.board.is_winner(player.piece):
                print(f"Herzlichen Glückwunsch {player.name}, du hast gewonnen!")
                break

            if self.board.is_full():
                print("Unentschieden! Das Spielfeld ist voll.")
                break

            self.switch_player()

if __name__ == "__main__":
    game = Game()
    game.play()
