import unittest
from src.board import Board

class TestBoard(unittest.TestCase):
    def test_drop_piece(self):
        board = Board()
        self.assertTrue(board.drop_piece(0, 'X'))
        self.assertEqual(board.board[-1][0], 'X')

    def test_is_winner_horizontal(self):
        board = Board()
        for i in range(4):
            board.drop_piece(i, 'X')
        self.assertTrue(board.is_winner('X'))

    def test_is_winner_vertical(self):
        board = Board()
        for i in range(4):
            board.drop_piece(0, 'X')
        self.assertTrue(board.is_winner('X'))

    def test_is_winner_diagonal(self):
        board = Board()
        board.drop_piece(0, 'X')
        board.drop_piece(1, 'O')
        board.drop_piece(1, 'X')
        board.drop_piece(2, 'O')
        board.drop_piece(2, 'O')
        board.drop_piece(2, 'X')
        board.drop_piece(3, 'O')
        board.drop_piece(3, 'O')
        board.drop_piece(3, 'O')
        board.drop_piece(3, 'X')
        self.assertTrue(board.is_winner('X'))

    def test_is_full(self):
        board = Board()
        for col in range(board.cols):
            for _ in range(board.rows):
                board.drop_piece(col, 'X')
        self.assertTrue(board.is_full())

if __name__ == '__main__':
    unittest.main()
