import unittest
from game import initialize_board, place_enemies


class TestPlaceEnemies(unittest.TestCase):
    def test_enemy_placement(self):
        board = initialize_board()
        num_enemies = place_enemies(board, 1)
        self.assertTrue(1 <= num_enemies <= 5)
        self.assertTrue(any(cell is not None for row in board for cell in row))