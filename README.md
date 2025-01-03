# 🌲 Mysterious Forest Game 🌲

Welcome to **Mysterious Forest**, a thrilling text-based adventure game where you navigate through a dangerous forest, fight exotic enemies, and face off against a mighty Boss! Your ultimate goal is to survive and reach the endpoint at **(4,4)**.

---

## 📋 Game Overview

- **Starting Position**: (0, 0) on a 5x5 grid.
- **Goal**: Navigate to **(4,4)** while battling enemies and surviving until the end.
- **Levels**: The game has **4 levels**, each increasing in difficulty:
  - **Enemies**: Health points increase with each level.
  - **Boss**: A **Dragon** with **10 HP** awaits in the final level.
- **Victory Condition**: Defeat the Boss and move to **(4,4)**.

---

## 🎮 How to Play

### **Instructions**
1. You start with **5 Health Points (HP)**.
2. At each level, enemies will spawn randomly across the board.

### **Movement**
Use the following keys to move:
- **W**: Move Up
- **A**: Move Left
- **S**: Move Down
- **D**: Move Right

### **Enemy Encounters**
- **Combat**: Type `kill` to attack the enemy.
  - Each `kill` reduces the enemy’s health by 1.
- **Hesitation**: Typing anything else will damage your health.

### **Boss Battle**
- Use `kill` to attack the Boss.
- Use `heal` to recover health.
- Beware! The Boss will retaliate with random damage.

---

Good luck, adventurer! Survive the **Mysterious Forest** and claim your victory! 🌟


| **Element**                | **Description**                                                                                                       | **Requirement Met**                                                                                                     |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Game Board Initialization** | Creates a 5x5 grid (list of lists) with empty cells, representing the game world.                                     | Implemented in `initialize_board`. Creates a dynamic board with proper dimensions, validated with doctests.              |
| **Random Enemy Placement**  | Distributes enemies on the game board randomly, ensuring no overlap and skipping certain fixed positions.             | Implemented in `place_enemies`. Ensures the number of enemies scales with levels and avoids key positions like (0, 0).   |
| **Enemy Encounter Mechanic** | Simulates combat mechanics when the player meets an enemy.                                                           | Implemented in `encounter_enemy`. Handles enemy health reduction, player hesitation, and victory/loss conditions.        |
| **Boss Battle Mechanic**    | Adds a special encounter with the Boss enemy in the final level.                                                     | Implemented in `boss_battle`. Includes healing mechanics and variable damage during combat with the Boss.                |
| **Player Movement**         | Allows players to navigate the grid using W/A/S/D keys and validates movement within bounds.                         | Implemented in `game`. Updates player position and prevents invalid moves with feedback.                                 |
| **Level Progression**       | Tracks levels, adds difficulty scaling (e.g., more enemies, stronger enemies), and restores player health per level. | Handled in `game`. Ensures level transitions after reaching the exit (4, 4).                                            |
| **Victory Conditions**      | Checks for player victory by defeating the Boss and moving to the final position (4, 4).                              | Implemented in `game`. Ends the game with a congratulatory message upon meeting victory conditions.                      |
| **Game Over Conditions**    | Ends the game when player health reaches 0 during any encounter or Boss battle.                                       | Handled in `encounter_enemy`, `boss_battle`, and `game`. Displays Game Over message if conditions are met.               |
| **Instructions Display**    | Provides detailed gameplay instructions, including movement, combat mechanics, and victory objectives.               | Implemented in `show_instructions`. Displays a clear and user-friendly guide at the start of the game.                   |
| **Dynamic Scaling**         | Adjusts difficulty through increased enemy health and count as levels progress.                                       | Implemented in `place_enemies` and `encounter_enemy`. Incorporates level-dependent scaling for more challenge.            |
| **Input Handling**          | Processes player commands for movement, combat, and healing during gameplay.                                         | Handled in `game`, `encounter_enemy`, and `boss_battle`. Includes input validation and meaningful feedback.               |
| **Testing and Validation**  | Ensures core functions behave as expected with examples and automated doctests.                                       | Implemented with doctests for key functions like `initialize_board`, `place_enemies`, and `encounter_enemy`.              |
| **User Feedback**           | Provides color-coded messages for enemy encounters, health changes, and game events using `colorama`.                | Implemented with `colorama` styles. Enhances the user experience with visual cues for combat and progression.             |
| **Replayability**           | Supports dynamic enemy placement and scaling for variability in gameplay.                                            | Achieved through `place_enemies` and randomization. Creates a unique game experience for each playthrough.                |