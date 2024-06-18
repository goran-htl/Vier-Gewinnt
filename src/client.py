import tkinter as tk
from tkinter import messagebox
from board import Board
from gui import Connect4GUI
import socket
import threading

def receive():
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg == 'CONNECTED':
                client_socket.send(nickName.encode('utf-8'))
            else:
                gui.draw_piece(int(msg))
                if board.check_winner('X'):
                    messagebox.showinfo("Spiel beendet", "Spieler X hat gewonnen!")
                    gui.reset_board()
                elif board.check_winner('O'):
                    messagebox.showinfo("Spiel beendet", "Spieler O hat gewonnen!")
                    gui.reset_board()
        except OSError:
            break

def main():
    global client_socket, nickName, gui, board

    IP = '127.0.0.1'
    PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    nickName = input("Enter your nickname: ")

    root = tk.Tk()
    gui = Connect4GUI(root)
    board = Board()

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    root.mainloop()

if __name__ == "__main__":
    main()
