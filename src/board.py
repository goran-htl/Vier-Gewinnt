class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    def drop_piece(self, col, piece):
        for row in reversed(range(self.rows)):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = piece
                return True
        return False  # Rückgabe False, wenn die Spalte voll ist

    def is_winner(self, piece):
        # Horizontal check
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row][col + i] == piece for i in range(4)):
                    return True

        # Vertical check
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.grid[row + i][col] == piece for i in range(4)):
                    return True

        # Positive diagonal check
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.grid[row + i][col + i] == piece for i in range(4)):
                    return True

        # Negative diagonal check
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.grid[row - i][col + i] == piece for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.grid[0][col] != ' ' for col in range(self.cols))

    def __str__(self):
        board_str = ""
        for row in self.grid:
            board_str += '|'.join(row) + "\n"
        return board_str
