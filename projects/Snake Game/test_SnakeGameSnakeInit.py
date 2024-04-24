# ********RoostGPT********
"""
Test generated by RoostGPT for test python-test using AI Type DBRX and AI Model dbrx-instruct

ROOST_METHOD_HASH=snake_game_Snake___init___292ac40af5
ROOST_METHOD_SIG_HASH=snake_game_Snake___init___f98f6ecd53

================================VULNERABILITIES================================
Vulnerability: CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer
Issue: The code uses the 'package' keyword, which is not a valid Python keyword. This may lead to unintended behavior or code injection vulnerabilities if this is user-supplied input.
Solution: Ensure that all user-supplied input is properly sanitized and validated before use. Use a linter or static code analyzer to catch such issues during development.

Vulnerability: CWE-327: Use of a Broken or Risky Cryptographic Algorithm
Issue: The 'tkinter' library, while useful for GUI development, is not suitable for cryptographic purposes. It is not designed to provide secure random number generation.
Solution: Instead of using 'random', consider using a cryptographically secure random number generator from Python's 'secrets' module or a well-maintained third-party library like 'cryptography'.

Vulnerability: CWE-20: Improper Input Validation
Issue: The code does not validate user input, such as the 'SPACE_SIZE' or 'SNAKE_COLOR' variables, which may lead to unintended behavior or security vulnerabilities.
Solution: Validate all user-supplied input and ensure that it conforms to expected formats and ranges. Use Python's built-in functions and libraries to perform input validation, such as 're' for regular expressions.

================================================================================
Scenario 1: Verify initial body size
  TestName: test_initial_body_size
  Description: This test ensures that the snake's initial body size is set to the specified value during initialization.
  Execution:
    Arrange: None
    Act: Create a new `Snake` instance with `snake = snake_game.Snake()`
    Assert: Check that `snake.body_size` equals `BODY_PARTS`
  Validation: The initial body size should be consistent with the specified value to ensure proper gameplay mechanics.

  Scenario 2: Verify initial coordinates
  TestName: test_initial_coordinates
  Description: This test verifies that the snake's initial coordinates are set to the correct values during initialization.
  Execution:
    Arrange: None
    Act: Create a new `Snake` instance with `snake = snake_game.Snake()`
    Assert: Check that `snake.coordinates` is a list of tuples, each containing two zeros
  Validation: The initial coordinates should be set correctly to ensure the snake's starting position on the game board.

  Scenario 3: Verify initial squares
  TestName: test_initial_squares
  Description: This test verifies that the snake's initial squares are created and added to the `squares` list during initialization.
  Execution:
    Arrange: None
    Act: Create a new `Snake` instance with `snake = snake_game.Snake()`
    Assert: Check that `snake.squares` is a list of `BODY_PARTS` rectangles, each with the correct dimensions and color
  Validation: The initial squares should be created and added to the list to ensure proper rendering on the game board.

  Scenario 4: Verify initial squares' coordinates
  TestName: test_initial_squares_coordinates
  Description: This test verifies that the initial squares' coordinates match the snake's coordinates during initialization.
  Execution:
    Arrange: None
    Act: Create a new `Snake` instance with `snake = snake_game.Snake()`
    Assert: Check that each square's coordinates match the corresponding tuple in `snake.coordinates`
  Validation: The initial squares' coordinates should match the snake's coordinates to ensure proper rendering on the game board.

  Scenario 5: Verify body size and squares list length
  TestName: test_body_size_and_squares_list_length
  Description: This test verifies that the length of the `squares` list matches the `body_size` during initialization.
  Execution:
    Arrange: None
    Act: Create a new `Snake` instance with `snake = snake_game.Snake()`
    Assert: Check that `len(snake.squares)` equals `snake.body_size`
  Validation: The length of the `squares` list should match the `body_size` to ensure proper gameplay mechanics and rendering.
"""

# ********RoostGPT********
from snake_game import Snake

def test_initial_body_size():
    snake = Snake()
    assert snake.body_size == BODY_PARTS

def test_initial_coordinates():
    snake = Snake()
    assert all(coord == [0, 0] for coord in snake.coordinates)

def test_initial_squares():
    snake = Snake()
    for square in snake.squares:
        assert canvas.itemcget(square, 'fill') == SNAKE_COLOR
        assert canvas.coords(square) == (0, 0, SPACE_SIZE, SPACE_SIZE)

def test_initial_squares_coordinates():
    snake = Snake()
    for coord, square in zip(snake.coordinates, snake.squares):
        assert canvas.coords(square) == (coord[0], coord[1], coord[0] + SPACE_SIZE, coord[1] + SPACE_SIZE)

def test_body_size_and_squares_list_length():
    snake = Snake()
    assert len(snake.squares) == snake.body_size
