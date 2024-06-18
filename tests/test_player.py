#Goran Nastasijevic

import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player("Player 1", 'X')
        self.assertEqual(player.name, "Player 1")
        self.assertEqual(player.piece, 'X')

if __name__ == '__main__':
    unittest.main()
