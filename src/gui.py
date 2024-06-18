import tkinter as tk
from tkinter import messagebox
from board import Board

class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.board = Board()
        self.current_player = 'X'
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Vier Gewinnt")

        self.buttons = []
        for col in range(self.board.cols):
            button = tk.Button(self.root, text=str(col), font=('Helvetica', 14), width=4,
                               command=lambda c=col: self.drop_piece(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        self.canvas = tk.Canvas(self.root, width=self.board.cols * 60, height=self.board.rows * 60)
        self.canvas.grid(row=1, columnspan=self.board.cols)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("pieces")
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.grid[row][col] != ' ':
                    color = 'yellow' if self.board.grid[row][col] == 'X' else 'red'
                    x0, y0 = col * 60 + 10, row * 60 + 10
                    x1, y1 = (col + 1) * 60 - 10, (row + 1) * 60 - 10
                    self.canvas.create_oval(x0, y0, x1, y1, fill=color, tags="pieces")

    def drop_piece(self, col):
        if self.board.drop_piece(col, self.current_player):
            self.draw_board()
            if self.board.check_winner(self.current_player):
                messagebox.showinfo("Spiel beendet", f"Spieler {self.current_player} hat gewonnen!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_board(self):
        self.board = Board()
        self.current_player = 'X'
        self.draw_board()

def main():
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
