# client.py

import tkinter as tk
import socket
import threading
from board import Board  # Importiere die Board-Klasse aus dem board-Modul

class VierGewinntGUI:
    def __init__(self, root, client_socket, nickname):
        self.root = root
        self.client_socket = client_socket
        self.nickname = nickname

        self.root.title("Vier Gewinnt")
        self.root.geometry("800x600")

        self.board = Board((6, 7))  # Initialisiere das Board mit der richtigen Größe

        self.buttons = []
        for col in range(self.board.cols):
            button = tk.Button(self.root, text=str(col), command=lambda c=col: self.drop_piece(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        self.message_label = tk.Label(self.root, text="")
        self.message_label.grid(row=1, column=0, columnspan=self.board.cols)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def drop_piece(self, col):
        self.client_socket.send(f"SPALTE:{col}".encode('utf-8'))

    def empfange(self):
        while True:
            nachricht = self.client_socket.recv(1024).decode('utf-8')
            if nachricht.startswith('SPALTE:'):
                _, spalte, farbe = nachricht.split(':')
                spalte = int(spalte)
                self.board.drop_piece(spalte, farbe)
                self.update_board()
            elif nachricht.startswith('GEWINNER:'):
                _, farbe = nachricht.split(':')
                self.message_label.config(text=f"{farbe} hat gewonnen!")
                self.board.reset()
                self.update_board()
            elif nachricht == 'DEIN ZUG':
                self.message_label.config(text="Dein Zug")
            else:
                print(nachricht)

    def update_board(self):
        for col in range(self.board.cols):
            for row in range(self.board.rows):
                color = 'white' if self.board.grid[row][col] == ' ' else self.board.grid[row][col]
                self.buttons[col].config(bg=color)

    def on_closing(self):
        self.client_socket.close()
        self.root.destroy()

def main():
    root = tk.Tk()

    IP = '127.0.0.1'
    PORT = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    nickname = input("Gib deinen Nickname ein: ").strip()

    gui = VierGewinntGUI(root, client_socket, nickname)
    gui.empfange()

    root.mainloop()

if __name__ == "__main__":
    main()
