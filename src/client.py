import tkinter as tk
from tkinter import messagebox
from board import Board
import socket
import threading

class VierGewinntGUI:
    def __init__(self, root, client_socket):
        self.root = root
        self.root.title("Vier Gewinnt")
        self.client_socket = client_socket

        self.buttons = []
        for spalte in range(7):
            button = tk.Button(self.root, text=str(spalte), command=lambda s=spalte: self.werfe_stein(s))
            button.grid(row=0, column=spalte)
            self.buttons.append(button)

        self.labels = [[tk.Label(self.root, text=" ", width=4, height=2, borderwidth=1, relief="solid")
                        for _ in range(7)] for _ in range(6)]
        for reihe in range(6):
            for spalte in range(7):
                self.labels[reihe][spalte].grid(row=reihe+1, column=spalte)

        self.board = Board()

    def werfe_stein(self, spalte):
        self.client_socket.send(f"SPALTE:{spalte}".encode('utf-8'))

    def zeichne_stein(self, spalte, farbe):
        self.board.drop_piece(spalte, farbe)
        self.aktualisiere_board()

    def aktualisiere_board(self):
        for reihe in range(6):
            for spalte in range(7):
                stein = self.board.grid[reihe][spalte]
                self.labels[reihe][spalte]['text'] = stein if stein != ' ' else ' '

    def reset_board(self):
        self.board = Board()
        self.aktualisiere_board()

def empfange():
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg == 'VERBUNDEN':
                client_socket.send(nickname.encode('utf-8'))
            elif msg.startswith('GEWINNER:'):
                winner = msg.split(':')[1]
                messagebox.showinfo("Spiel beendet", f"{winner} gewinnt!")
                gui.reset_board()
            elif msg.startswith('SPALTE:'):
                spalte = int(msg.split(':')[1])
                farbe = 'X' if len(gui.board.grid[0]) % 2 == 0 else 'O'
                gui.zeichne_stein(spalte, farbe)
            else:
                messagebox.showinfo("Nachricht", msg)
        except OSError:
            break

def main():
    global client_socket, nickname, gui

    IP = '127.0.0.1'
    PORT = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    nickname = input("Gib deinen Nickname ein: ")

    root = tk.Tk()
    gui = VierGewinntGUI(root, client_socket)

    empfange_thread = threading.Thread(target=empfange)
    empfange_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()

