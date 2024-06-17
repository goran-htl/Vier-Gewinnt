import unittest
from src.game import Game
from src.board import Board
from src.player import Player

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        game = Game()
        self.assertIsInstance(game.board, Board)
        self.assertEqual(len(game.players), 2)
        self.assertIsInstance(game.players[0], Player)
        self.assertIsInstance(game.players[1], Player)
        self.assertEqual(game.current_player, 0)

    # Hier können weitere Tests hinzugefügt werden

if __name__ == '__main__':
    unittest.main()