#Goran Nastasijevic
#Furkan Gueyen

import tkinter as tk
from tkinter import messagebox
from board import Board  # Import der Board-Klasse aus board.py
from player import Player  # Import der Player-Klasse aus player.py


class ConnectFourGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vier Gewinnt")  # Fenstertitel festlegen

        self.board = Board()  # Initialisierung des Spielbretts
        self.players = [Player("Player 1", 'X'), Player("Player 2", 'O')]  # Initialisierung der Spieler
        self.current_player = 0  # Index des aktuellen Spielers (0 für Spieler 1)

        self.create_widgets()  # Erstellen der GUI-Elemente

    def create_widgets(self):
        # Erstellen der Buttons für jede Spalte
        self.buttons = []
        for col in range(self.board.cols):
            button = tk.Button(self.root, text=str(col), command=lambda c=col: self.drop_piece(c))
            button.grid(row=0, column=col)  # Buttons in der obersten Reihe platzieren
            self.buttons.append(button)

        # Erstellen der Labels für das Spielbrett
        self.labels = []
        for row in range(1, self.board.rows + 1):
            row_labels = []
            for col in range(self.board.cols):
                label = tk.Label(self.root, text=' ', width=5, height=2, borderwidth=2, relief="groove")
                label.grid(row=row, column=col)  # Labels für das Spielbrett platzieren
                row_labels.append(label)
            self.labels.append(row_labels)

    def drop_piece(self, col):
        player = self.players[self.current_player]  # Aktuellen Spieler auswählen
        if self.board.drop_piece(col, player.piece):  # Versuch, einen Spielstein fallen zu lassen
            self.update_board()  # Spielbrett in der GUI aktualisieren
            if self.board.is_winner(player.piece):  # Überprüfen, ob der Spieler gewonnen hat
                messagebox.showinfo("Spielende", f"{player.name} hat gewonnen!")  # Gewinnmeldung anzeigen
                self.reset_board()  # Spielbrett zurücksetzen
            elif self.board.is_full():  # Überprüfen, ob das Spielbrett voll ist
                messagebox.showinfo("Spielende", "Unentschieden! Das Spielfeld ist voll.")  # Unentschieden anzeigen
                self.reset_board()  # Spielbrett zurücksetzen
            else:
                self.current_player = (self.current_player + 1) % 2  # Nächsten Spieler auswählen
        else:
            messagebox.showwarning("Ungültiger Zug", "Diese Spalte ist voll. Bitte wähle eine andere Spalte.")  # Warnung für ungültigen Zug anzeigen

    def update_board(self):
        # Spielbrett in der GUI aktualisieren
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                piece = self.board.grid[row][col]
                self.labels[row][col].config(text=piece if piece else ' ')

    def reset_board(self):
        # Spielbrett zurücksetzen
        self.board = Board()  # Neues Spielbrett initialisieren
        self.current_player = 0  # Index des aktuellen Spielers zurücksetzen
        self.update_board()  # Spielbrett in der GUI aktualisieren


if __name__ == "__main__":
    root = tk.Tk()  # Hauptfenster erstellen
    app = ConnectFourGUI(root)  # Instanz der ConnectFourGUI erstellen
    root.mainloop()  # Hauptfenster ausführen
