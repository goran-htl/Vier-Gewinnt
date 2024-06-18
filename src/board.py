#Goran Nastasijevic

class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows  # Anzahl der Zeilen auf dem Spielbrett
        self.cols = cols  # Anzahl der Spalten auf dem Spielbrett
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]  # Erzeugt eine leere Spielbrett-Matrix

    def drop_piece(self, col, piece):
        # Platzierung eines Spielsteins in einer bestimmten Spalte
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = piece
                return True
        return False  # Rückgabe False, wenn die Spalte voll ist und kein Spielstein platziert werden kann

    def is_winner(self, piece):
        # Überprüfung auf Gewinner in horizontaler Richtung
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row][col + i] == piece for i in range(4)):
                    return True

        # Überprüfung auf Gewinner in vertikaler Richtung
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.grid[row + i][col] == piece for i in range(4)):
                    return True

        # Überprüfung auf Gewinner in positiver Diagonale
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.grid[row + i][col + i] == piece for i in range(4)):
                    return True

        # Überprüfung auf Gewinner in negativer Diagonale
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row - i][col + i] == piece for i in range(4)):
                    return True

        return False  # Rückgabe False, wenn kein Gewinner gefunden wurde

    def is_full(self):
        # Überprüfung, ob das Spielbrett voll ist (keine leeren Felder mehr vorhanden sind)
        return all(self.grid[0][col] != ' ' for col in range(self.cols))

    def __str__(self):
        # Rückgabe einer Zeichenfolge, die das Spielbrett darstellt
        board_str = ""
        for row in self.grid:
            board_str += '|'.join(row) + "\n"
        return board_str
