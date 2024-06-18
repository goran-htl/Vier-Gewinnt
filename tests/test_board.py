import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_drop_piece(self):
        board = Board()
        self.assertTrue(board.drop_piece(0, 'X'))
        self.assertEqual(board.grid[-1][0], 'X')  # Hier sollte 'grid' anstelle von 'board' verwendet werden
        self.assertFalse(board.drop_piece(0, 'X'))

    def test_is_winner(self):
        board = Board()
        for i in range(4):
            board.drop_piece(i, 'X')
        self.assertTrue(board.is_winner('X'))

    def test_is_full(self):
        board = Board()
        for col in range(board.cols):
            for row in range(board.rows):
                board.drop_piece(col, 'X')
        self.assertTrue(board.is_full())


if __name__ == '__main__':
    unittest.main()
