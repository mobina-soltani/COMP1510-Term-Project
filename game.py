import random
from itertools import cycle
from unittest.mock import patch
from colorama import Fore, Style, init


def initialize_board() -> list:
    """
    Initialize the game board as a dictionary.

    The board represents a 5x5 grid where each coordinate (x, y) is a key, and the value is the cell's description.
    Cells are initially empty.

    :return: dict: A dictionary representing the board where keys are (x, y) tuples and values are descriptions as strings.

    >>> board = initialize_board()
    >>> len(board)
    5
    >>> all(len(row) == 5 for row in board)
    True
    >>> all(cell is None for row in board for cell in row)
    True
    """
    return [[None for _ in range(5)] for _ in range(5)]


def place_enemies(board: list, level: int) -> int:
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
    enemy_positions = cycle([(0, 1), (1, 2), (2, 3), (3, 4)])  # Using itertools
    enemy_count = 0

    while enemy_count < num_enemies:
        x, y = next(enemy_positions) if enemy_count < 4 else (random.randint(0, 4), random.randint(0, 4))
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
    print(Fore.RED + f"\n⚔️ You have encountered a {enemy_name}!")
    while enemy_health > 0:
        print(Fore.YELLOW + f"The {enemy_name}'s health: {enemy_health}")
        action = input(Fore.CYAN + "Type 'kill' to attack: ").lower()
        if action == "kill":
            enemy_health -= 1
            print(Fore.GREEN + "🔥 You attacked the enemy!")
        else:
            print(Fore.RED + "⚠️ You hesitated, and the enemy attacks you!")
            player_health -= 1
        if player_health <= 0:
            print(Fore.RED + "💀 You have been defeated by the enemy!")
            return player_health, False
    print(Fore.GREEN + f"\n🎉 You defeated the {enemy_name}!")
    return player_health, True


def boss_battle(player_health):
    """
    Simulates the boss battle after the player entered the coordinates, (3,4) or (4,3) at level 4.

    The player must enter heal to add up health points and kill to damage the boss.

    :param:player_health (int): Player's current health.
    :return:tuple: Remaining player health and victory status (True if the player wins, False if defeated).

    >>> random.seed(0)
    >>> inputs = iter(["kill", "kill", "kill", "heal", "kill", "kill", "kill", "kill", "kill", "kill"])
    >>> with patch('builtins.input', lambda _: next(inputs)):
    ...     boss_battle(20)
    (15, True)

    >>> random.seed(0)
    >>> inputs = iter(["hesitate", "hesitate", "kill", "kill", "hesitate", "kill"])
    >>> with patch('builtins.input', lambda _: next(inputs)):
    ...     boss_battle(10)
    (0, False)
    """
    boss_health = 10
    print(Fore.MAGENTA + "\n🐉 You have encountered the Boss! A fierce Dragon awaits.")
    while player_health > 0 and boss_health > 0:
        print(Fore.RED + f"Boss's Health: {boss_health}")
        print(Fore.BLUE + f"Your Health: {player_health}")
        action = input(Fore.CYAN + "Type 'kill' to attack the boss or 'heal' to heal: ").lower()
        if action == "kill":
            boss_health -= 1
            print(Fore.GREEN + "🔥 You attacked the boss!")
        elif action == "heal":
            heal = random.randint(2, 5)
            player_health += heal
            print(Fore.GREEN + f"💊 You healed yourself for {heal} HP.")
        else:
            print(Fore.RED + "⚠️ You hesitated, and the boss strikes!")
        boss_damage = random.randint(2, 4)
        player_health -= boss_damage
        print(Fore.RED + f"💥 The boss attacked you for {boss_damage} damage!")
    return player_health > 0


def show_instructions():
   """
   Explains the game instructions and mechanics to the player.
   """
   print(Fore.BLUE + Style.BRIGHT + "\n" + "=" * 40)
   print(Fore.YELLOW + Style.BRIGHT + "🌲 Welcome to the Mysterious Forest 🌲")
   print(Fore.BLUE + Style.BRIGHT + "=" * 40)
   print(Fore.CYAN + "\n--- Instructions ---")
   print("1. Your goal is to move from (0,0) to (4,4) while surviving enemies and battles.")
   print("2. You start the game with 5 health points (HP).")
   print("3. In each level, enemies have health points equal to level + 2.")
   print("4. To defeat an enemy, type 'kill' 3 times, reducing their health by 1 each time.")
   print("5. In the final level, you must defeat a Boss with 10 HP located at (4,3) and (3,4).")
   print("6. Once you defeat the Boss, you can move to (4,4) to win the game!")
   print("\n--- Movement ---")
   print("Move using W (up), A (left), S (down), or D (right).")
   print(Fore.BLUE + Style.BRIGHT + "=" * 40)


def game():
    show_instructions()
    character_name = input(Fore.CYAN + "\nEnter your character's name: ")
    print(Fore.GREEN + f"\nWelcome, {character_name}, to the Mysterious Forest!")
    player_health = 5
    level = 1

    while level <= 4:
        print(Fore.YELLOW + f"\n🌟 Level {level} begins! 🌟")
        board = initialize_board()
        place_enemies(board, level)
        player_pos = (0, 0)

        while player_pos != (4, 4) and player_health > 0:
            print(Fore.CYAN + f"\nYour HP: {player_health}")
            print(Fore.GREEN + f"Your current position: {player_pos}")
            print("Move using W/A/S/D:")
            move = input(Fore.CYAN + "> ").upper()

            x, y = player_pos
            if move == "W" and x > 0:
                x -= 1
            elif move == "A" and y > 0:
                y -= 1
            elif move == "S" and x < 4:
                x += 1
            elif move == "D" and y < 4:
                y += 1
            else:
                print(Fore.RED + "❌ Invalid move! Try again.")
                continue

            player_pos = (x, y)

            if board[x][y] is not None:
                enemy_name = board[x][y]
                if enemy_name == "Boss" and level == 4:
                    if boss_battle(player_health):
                        print(Fore.MAGENTA + "\n🎉 You have defeated the Boss!")
                        board[x][y] = None  # Boss defeated
                    else:
                        player_health = 0
                        break
                else:
                    enemy_health = level + 2  # Enemy health increases with level
                    player_health, victory = encounter_enemy(enemy_name, player_health, enemy_health)
                    if victory:
                        board[x][y] = None  # Remove enemy after encounter
                    else:
                        break

        if player_health <= 0:
            print(Fore.RED + "\n💀 Game Over! Better luck next time.")
            break

        if player_pos == (4, 4):
            if level == 4:
                print(Fore.GREEN + "\n🎉 Congratulations! You have defeated the Dragon and completed the game!")
            else:
                print(Fore.YELLOW + f"\n🎉 Congratulations! You have completed Level {level}.")
                level += 1
                player_health += 3  # Restore some health after level up
                print(Fore.GREEN + f"\n💊 Your health has been restored to {player_health}!")

    print(Fore.BLUE + "\n🌲 Thanks for playing Mysterious Forest! 🌲")


if __name__ == "__main__":
    game()