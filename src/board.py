class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]

    def drop_piece(self, col, piece):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = piece
                return True
        return False

    def check_winner(self, piece):
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if self.grid[row][col] == piece and \
                   self.grid[row][col+1] == piece and \
                   self.grid[row][col+2] == piece and \
                   self.grid[row][col+3] == piece:
                    return True

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if self.grid[row][col] == piece and \
                   self.grid[row+1][col] == piece and \
                   self.grid[row+2][col] == piece and \
                   self.grid[row+3][col] == piece:
                    return True

        # Check diagonal (down-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if self.grid[row][col] == piece and \
                   self.grid[row+1][col+1] == piece and \
                   self.grid[row+2][col+2] == piece and \
                   self.grid[row+3][col+3] == piece:
                    return True

        # Check diagonal (up-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if self.grid[row][col] == piece and \
                   self.grid[row-1][col+1] == piece and \
                   self.grid[row-2][col+2] == piece and \
                   self.grid[row-3][col+3] == piece:
                    return True

        return False

