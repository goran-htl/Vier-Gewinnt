class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(7)] for _ in range(6)]

    def drop_piece(self, col, piece):
        for row in range(5, -1, -1):
            if self.grid[row][col] == ' ':
                self.grid[row][col] = piece
                return True
        return False

    def check_winner(self, piece):
        for row in range(6):
            for col in range(7):
                if self.check_line(piece, row, col, 1, 0) or \
                   self.check_line(piece, row, col, 0, 1) or \
                   self.check_line(piece, row, col, 1, 1) or \
                   self.check_line(piece, row, col, 1, -1):
                    return True
        return False

    def check_line(self, piece, row, col, drow, dcol):
        for i in range(4):
            r = row + i * drow
            c = col + i * dcol
            if r < 0 or r >= 6 or c < 0 or c >= 7 or self.grid[r][c] != piece:
                return False
        return True

    def reset(self):
        self.grid = [[' ' for _ in range(7)] for _ in range(6)]
