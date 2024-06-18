#Goran Nastasijevic
import unittest
from game import ConnectFourCLI
from board import Board


class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = ConnectFourCLI()
        self.assertIsInstance(game.board, Board)
        self.assertEqual(game.board.rows, 6)
        self.assertEqual(game.board.cols, 7)

    def test_switch_player(self):
        game = ConnectFourCLI()
        first_player = game.current_player
        game.switch_player()
        self.assertNotEqual(game.current_player, first_player)


if __name__ == '__main__':
    unittest.main()