import unittest
from random import random
from unittest.mock import patch
from game import boss_battle


class TestBossBattle(unittest.TestCase):
    def test_player_wins(self):
        random.seed(0)  # Deterministic behavior
        inputs = iter(["kill", "kill", "kill", "heal", "kill", "kill", "kill", "kill", "kill", "kill"])
        with patch('builtins.input', lambda _: next(inputs)):
            player_health, victory = boss_battle(20)
        self.assertEqual(player_health, 15)
        self.assertTrue(victory)

    def test_player_loses(self):
        random.seed(0)  # Deterministic behavior
        inputs = iter(["hesitate", "hesitate", "kill", "kill", "hesitate", "kill"])
        with patch('builtins.input', lambda _: next(inputs)):
            player_health, victory = boss_battle(10)
        self.assertEqual(player_health, 0)
        self.assertFalse(victory)
