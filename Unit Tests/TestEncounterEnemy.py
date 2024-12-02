import unittest
from unittest.mock import patch

from game import encounter_enemy

class TestEncounterEnemy(unittest.TestCase):
    @patch('builtins.input', side_effect=['kill', 'kill', 'kill'])
    def test_enemy_defeat(self, mock_input):
        player_health, victory = encounter_enemy("Tiger", 5, 3)
        self.assertTrue(victory)
        self.assertEqual(player_health, 5)
