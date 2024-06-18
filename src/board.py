# Goran Nastasijevic

class Board:
    def __init__(self, dimension_sizes):
        self.rows, self.cols = dimension_sizes
        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def drop_piece(self, col, piece):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = piece
                return True
        return False

    def check_winner(self, piece):
        # Implementiere die Logik zur Überprüfung auf einen Gewinner
        pass

    def reset(self):
        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
