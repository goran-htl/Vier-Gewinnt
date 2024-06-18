# game.py

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
        print("Welcome to Connect Four!")
        print(self.board)

        while True:
            player = self.players[self.current_player]
            col = int(input(f"{player.name} ({player.piece}), choose a column (0-{self.board.cols-1}): "))

            if col < 0 or col >= self.board.cols or not self.board.drop_piece(col, player.piece):
                print("Invalid move. Please try again.")
                continue

            print(self.board)

            if self.board.is_winner(player.piece):
                print(f"Congratulations {player.name}, you won!")
                break

            if self.board.is_full():
                print("Draw! The board is full.")
                break

            self.switch_player()

if __name__ == "__main__":
    game = ConnectFourCLI()
    game.play()
