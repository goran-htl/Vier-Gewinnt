class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]

    def drop_piece(self, col, piece):
        for row in reversed(range(self.rows)):
            if self.board[row][col] == ' ':
                self.board[row][col] = piece
                return True
        return False

    def is_winner(self, piece):
        # Check horizontal locations
        for c in range(self.cols - 3):
            for r in range(self.rows):
                if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][c + 3] == piece:
                    return True

        # Check vertical locations
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(self.cols - 3):
            for r in range(self.rows - 3):
                if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.cols - 3):
            for r in range(3, self.rows):
                if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and self.board[r - 3][c + 3] == piece:
                    return True

        return False

    def is_full(self):
        return all(self.board[0][c] != ' ' for c in range(self.cols))

    def __str__(self):
        display = ""
        for row in self.board:
            display += '|'.join(row) + '\n'
        display += '-' * (2 * self.cols - 1) + '\n'
        display += ' '.join(str(i) for i in range(self.cols)) + '\n'
        return display
