#Goran Nastasijevic

import unittest
from tkinter import Tk
from src.gui import ConnectFourGUI

class TestConnectFourGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = ConnectFourGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initial_setup(self):
        self.assertEqual(len(self.app.buttons), 7)
        self.assertEqual(len(self.app.labels), 6)
        self.assertEqual(len(self.app.labels[0]), 7)

    def test_drop_piece(self):
        self.app.drop_piece(0)
        self.assertEqual(self.app.board.grid[5][0], 'X')
        self.app.drop_piece(0)
        self.assertEqual(self.app.board.grid[4][0], 'O')

if __name__ == "__main__":
    unittest.main()
