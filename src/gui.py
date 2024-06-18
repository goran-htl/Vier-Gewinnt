import tkinter as tk
from tkinter import messagebox
from board import Board
from player import Player


class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vier Gewinnt")

        self.board = Board()
        self.players = [Player("Player 1", 'X'), Player("Player 2", 'O')]
        self.current_player = 0

        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for col in range(self.board.cols):
            button = tk.Button(self.root, text=str(col), command=lambda c=col: self.drop_piece(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        self.labels = []
        for row in range(1, self.board.rows + 1):
            row_labels = []
            for col in range(self.board.cols):
                label = tk.Label(self.root, text=' ', width=5, height=2, borderwidth=2, relief="groove")
                label.grid(row=row, column=col)
                row_labels.append(label)
            self.labels.append(row_labels)

    def drop_piece(self, col):
        player = self.players[self.current_player]
        if self.board.drop_piece(col, player.piece):
            self.update_board()
            if self.board.is_winner(player.piece):
                messagebox.showinfo("Spielende", f"{player.name} hat gewonnen!")
                self.reset_board()
            elif self.board.is_full():
                messagebox.showinfo("Spielende", "Unentschieden! Das Spielfeld ist voll.")
                self.reset_board()
            else:
                self.current_player = (self.current_player + 1) % 2
        else:
            messagebox.showwarning("Ungültiger Zug", "Diese Spalte ist voll. Bitte wähle eine andere Spalte.")

    def update_board(self):
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                piece = self.board.grid[row][col]
                self.labels[row][col].config(text=piece if piece else ' ')

    def reset_board(self):
        self.board = Board()
        self.current_player = 0
        self.update_board()


if __name__ == "__main__":
    root = tk.Tk()
    app = ConnectFourGUI(root)
    root.mainloop()
