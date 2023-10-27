import unittest
import snake_game
from unittest.mock import Mock

'''
Test Scenarios
 
Test Scenario 1: Snake's x coordinate is less than zero.
- Given: A snake object with initial coordinates (-1, 5).
- Expected: The function should return True.

Test Scenario 2: Snake's x coordinate is equal to the GAME_WIDTH.
- Given: A snake object with initial coordinates (GAME_WIDTH, 10), where GAME_WIDTH is a constant defining the width of the game area.
- Expected: The function should return True.

Test Scenario 3: Snake's y coordinate is less than zero.
- Given: A snake object with initial coordinates (10, -1).
- Expected: The function should return True.

Test Scenario 4: Snake's y coordinate is equal to the GAME_HEIGHT.
- Given: A snake object with initial coordinates (10, GAME_HEIGHT), where GAME_HEIGHT is a constant defining the height of the game area.
- Expected: The function should return True.

Test Scenario 5: The snake's head (first coordinate pair) collides with another body part.
- Given: A snake object with coordinates [(10, 5), (10, 6), (10, 7), (10, 5)].
- Expected: The function should return True.

Test Scenario 6: The snake does not collide with the boundaries or with itself.
- Given: A snake object with coordinates [(10, 5), (11, 6), (12, 7)].
- Expected: The function should return False.

Test Scenario 7: Edge case where the snake object has all coordinates falling within the game window and does not collide with itself.
- Given: A snake object with coordinates [(0, 0), (0, 1), (1, 1), (1, 2)].
- Expected: The function should return False.

Test Scenario 8: Edge case where snake object has only one coordinate and it falls within the game window.
- Given: A snake object with coordinates [(GAME_WIDTH-1, GAME_HEIGHT-1)].
- Expected: The function should return False.  

Test Scenario 9: Edge case where snake object has only one coordinate and it falls outside game window.
- Given: A snake object with coordinates [(GAME_WIDTH+1, GAME_HEIGHT+1)].
- Expected: The function should return True.  

Test Scenario 10: Edge case where snake object has more than two identical coordinates.
- Given: A snake object with coordinates [(10, 10), (10, 10), (10, 10)].
- Expected: The function should return True. 
'''

class TestCheckCollisions(unittest.TestCase):
    def setUp(self):
        self.snake = Mock()

    def test_x_less_than_zero(self):
        self.snake.coordinates = [(-1, 5)]
        self.assertTrue(snake_game.check_collisions(self.snake))

    def test_x_equal_game_width(self):
        self.snake.coordinates = [(snake_game.GAME_WIDTH, 10)]
        self.assertTrue(snake_game.check_collisions(self.snake))

    def test_y_less_than_zero(self):
        self.snake.coordinates = [(10, -1)]
        self.assertTrue(snake_game.check_collisions(self.snake))

    def test_y_equal_game_height(self):
        self.snake.coordinates = [(10, snake_game.GAME_HEIGHT)]
        self.assertTrue(snake_game.check_collisions(self.snake))

    def test_head_collides_with_body_part(self):
        self.snake.coordinates = [(10, 5), (10, 6), (10, 7), (10, 5)]
        self.assertTrue(snake_game.check_collisions(self.snake))

    def test_no_collisions(self):
        self.snake.coordinates = [(10, 5), (11, 6), (12, 7)]
        self.assertFalse(snake_game.check_collisions(self.snake))

    def test_edge_case_within_boundary_no_self_collision(self):
        self.snake.coordinates = [(0, 0), (0, 1), (1, 1), (1, 2)]
        self.assertFalse(snake_game.check_collisions(self.snake))

    def test_edge_case_one_coordinate_within_boundaries(self):
        self.snake.coordinates = [(snake_game.GAME_WIDTH-1, snake_game.GAME_HEIGHT-1)]
        self.assertFalse(snake_game.check_collisions(self.snake))

    def test_edge_case_one_coordinate_outside_boundaries(self):
        self.snake.coordinates = [(snake_game.GAME_WIDTH+1, snake_game.GAME_HEIGHT+1)]
        self.assertTrue(snake_game.check_collisions(self.snake))

    def test_edge_case_more_than_two_identical_coordinates(self):
        self.snake.coordinates = [(10, 10), (10, 10), (10, 10)]
        self.assertTrue(snake_game.check_collisions(self.snake))

if __name__ == '__main__':
    unittest.main(verbosity=2)
