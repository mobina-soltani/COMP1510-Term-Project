import unittest
from game import initialize_board


class TestInitializeBoard(unittest.TestCase):
    def test_board_structure(self):
        board = initialize_board()
        self.assertEqual(len(board), 5)
        self.assertTrue(all(len(row) == 5 for row in board))
        self.assertTrue(all(cell is None for row in board for cell in row))
if __name__ == "__main__":
    unittest.main()
