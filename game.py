

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
    """
