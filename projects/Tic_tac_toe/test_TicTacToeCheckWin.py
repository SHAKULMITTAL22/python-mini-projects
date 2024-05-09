# ********RoostGPT********
"""
Test generated by RoostGPT for test python-test using AI Type Open AI and AI Model gpt-4-turbo

ROOST_METHOD_HASH=check_win_ff81222f30
ROOST_METHOD_SIG_HASH=check_win_e1e4c7287d

### Scenario 1: All squares in a winning condition are occupied by the same player
Details:
  TestName: test_check_win_all_squares_same_player
  Description: This test verifies that the function returns True when all squares in any of the winning conditions are occupied by the same player.
Execution:
  Arrange: Define `win_conditions` with at least one set of indices and initialize `squares` such that the indices in one of the win conditions are all occupied by the same player.
  Act: Call `check_win` with the player who occupies the winning condition.
  Assert: Check that the function returns True.
Validation:
  This test confirms that the function correctly identifies a win when a player occupies all squares in any of the predefined winning conditions. This is a fundamental requirement for the function to meet the game's win detection logic.

### Scenario 2: No winning condition met
Details:
  TestName: test_check_win_no_condition_met
  Description: This test ensures that the function returns False when no winning condition is fully occupied by the same player.
Execution:
  Arrange: Define `win_conditions` and initialize `squares` such that no set of indices in any win condition is occupied entirely by the same player.
  Act: Call `check_win` with any player.
  Assert: Check that the function returns False.
Validation:
  This test is crucial to ensure that the function does not falsely declare a winner when the conditions for winning are not met. It helps maintain the integrity of the game's rules.

### Scenario 3: Some squares in a winning condition are occupied by the same player
Details:
  TestName: test_check_win_partial_occupation
  Description: This test checks that the function returns False when only some (but not all) squares in a winning condition are occupied by the same player.
Execution:
  Arrange: Define `win_conditions` and initialize `squares` such that only some of the indices in one of the win conditions are occupied by the same player.
  Act: Call `check_win` with the player who partially occupies the condition.
  Assert: Check that the function returns False.
Validation:
  This scenario tests the function's ability to correctly identify that a win has not occurred despite partial occupation of a win condition. It ensures that the function strictly requires full occupation of a win condition to declare a win.

### Scenario 4: Winning condition met with mixed players
Details:
  TestName: test_check_win_mixed_players
  Description: This test verifies that the function returns False when squares in a winning condition are occupied by different players.
Execution:
  Arrange: Define `win_conditions` and initialize `squares` such that all indices in one of the win conditions are occupied, but not exclusively by one player.
  Act: Call `check_win` with one of the players.
  Assert: Check that the function returns False.
Validation:
  This test ensures that the function correctly identifies that no win has occurred when a win condition is filled by multiple players. It is essential for maintaining the game's fairness and rule enforcement.

### Scenario 5: Winning condition met exactly
Details:
  TestName: test_check_win_exact_match
  Description: This test ensures that the function returns True when exactly the squares in one of the win conditions are occupied by the same player, with no additional squares occupied.
Execution:
  Arrange: Define `win_conditions` and initialize `squares` such that exactly the indices in one of the win conditions are occupied by the same player, and all other squares are empty or occupied by another player.
  Act: Call `check_win` with the player occupying the win condition.
  Assert: Check that the function returns True.
Validation:
  This scenario ensures that the function can correctly identify a win even when the winning condition is met without any additional squares being occupied. This helps in verifying the precision of the win detection logic in scenarios where the minimum required conditions for a win are met.
"""

# ********RoostGPT********
# tic_tac_toe.py

def check_win(squares, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for condition in win_conditions:
        if all(squares[i] == player for i in condition):
            return True
    return False
