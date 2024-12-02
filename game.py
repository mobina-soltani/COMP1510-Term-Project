import random
from unittest.mock import patch


def initialize_board():
    """
    Initialize the game board as a dictionary.

    The board represents a 5x5 grid where each coordinate (x, y) is a key, and the value is the cell's description.
    Cells are initially empty.

    Return: dict: A dictionary representing the board where keys are (x, y) tuples and values are descriptions as strings.

    >>> board = initialize_board()
    >>> len(board)
    5
    >>> all(len(row) == 5 for row in board)
    True
    >>> all(cell is None for row in board for cell in row)
    True
    """
    return [[None for _ in range(5)] for _ in range(5)]


def place_enemies(board, level):
    """
    Places enemies randomly on the board based on the level.

    The number and type of enemies are determined by the level. Enemies are
    placed in random positions, ensuring no overlap and avoiding the player's
    starting position or the boss's fixed locations.

    :param: board (list): A 5x5 game board represented as a list of lists.
            level (int): The current level of the game, affecting the number of enemies.
    :return: int: The number of enemies placed on the board.

    >>> board = initialize_board()
    >>> num_enemies = place_enemies(board, 1)
    >>> 1 <= num_enemies <= 5
    True
    >>> any(cell is not None for row in board for cell in row)
    True
    """
    enemies = ["Tiger", "Snake", "Panther", "Crocodile", "Jaguar"]
    num_enemies = int(5 * (1 + (level - 1) * 0.5))
    enemy_count = 0
    while enemy_count < num_enemies:
        x, y = random.randint(0, 4), random.randint(0, 4)
        if board[x][y] is None and (x, y) not in [(0, 0), (4, 3), (3, 4), (4, 4)]:
            board[x][y] = random.choice(enemies)
            enemy_count += 1

    # Place the boss at fixed locations for the final level
    if level == 4:
        board[4][3] = "Boss"
        board[3][4] = "Boss"
    return num_enemies


def encounter_enemy(enemy_name, player_health, enemy_health):
    """
    Handles the player's interaction with an enemy during an encounter.

    The player must type 'kill' to attack the enemy and reduce its health.
    If the player hesitates (not type 'kill'), they get damage.
    The encounter ends when either the player or the enemy's health gets 0.

    :param:enemy_name (str): The name of the enemy encountered.
            player_health (int): The player's current health points.
            enemy_health (int): The enemy's current health points.

    :return:tuple:
            - int: Remaining health of the player.
            - bool: `True` if the player defeats the enemy, `False` otherwise.

    >>> inputs = iter(["kill", "kill", "kill"])
    >>> with patch('builtins.input', lambda _: next(inputs)):
    ...     encounter_enemy("Tiger", 5, 3)
    (5, True)

    >>> inputs = iter(["hesitate", "kill", "kill", "kill"])
    >>> with patch('builtins.input', lambda _: next(inputs)):
    ...     encounter_enemy("Snake", 5, 3)
    (4, True)

    >>> inputs = iter(["hesitate", "hesitate", "hesitate", "kill", "kill"])
    >>> with patch('builtins.input', lambda _: next(inputs)):
    ...     encounter_enemy("Panther", 3, 3)
    (0, False)
    """


