import unittest
from unittest.mock import Mock
# import other dependencies
'''
 Make sure to import accordingly. I have left it to as a comment as I cannot validate the exact import you might need.
 The dependencies needed may vary depending on what the project needs.
'''

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()  # Assuming that Snake is a class in your project
        self.BODY_PARTS = BODY_PARTS
        self.SPACE_SIZE = SPACE_SIZE
       
    def test_initialization(self):
        self.assertEqual(self.snake.body_size, self.BODY_PARTS, "body_size should be initialized to BODY_PARTS constant value.")
        self.assertIsInstance(self.snake.coordinates, list, "Expected object type is list for 'coordinates'")
        self.assertIsInstance(self.snake.squares, list, "Expected object type is list for 'squares'")
        self.assertEqual(self.snake.coordinates, [[0, 0] for _ in range(self.BODY_PARTS)], "Expected coordinates with BODY_PARTS number of [[0,0]] elements")

    def test_squares_creation(self):
        canvas.create_rectangle = Mock()  # This is creating a Mocked function for 'canvas.create_rectangle'
        for _ in range(self.BODY_PARTS):
            self.snake.create_square()  # Assuming that create_square is a method in your Snake class

        expected_calls = [((0, 0, self.SPACE_SIZE, self.SPACE_SIZE), {'fill': SNAKE_COLOR, 'tag': 'snake'}) for _ in range(self.BODY_PARTS)]
        
        # Here we're testing that the canvas.create_rectangle method is called with the right parameters
        self.assertEqual(canvas.create_rectangle.call_args_list, expected_calls, "Each coordinate should create a square with correct size and color")
        
        # Test if square has been added to squares list
        self.assertEqual(len(self.snake.squares), self.BODY_PARTS, "Expected squares to contain number of elements equals to BODY_PARTS")

    def test_variable_types(self):
        self.assertIsInstance(self.snake.body_size, int, "Expected object type is int for 'body_size'")
        for coord in self.snake.coordinates:
            self.assertIsInstance(coord, list, "Expected object type is list for each coordinate")
            for element in coord:
                self.assertIsInstance(element, int, "Expected object type is int for each element of individual coordinate")

        # Assuming that square is an object of a certain class in your project 
        square = self.snake.squares[0] if self.snake.squares else None
        self.assertTrue(all(isinstance(sq, type(square)) for sq in self.snake.squares), "Expected object type is the same as 'square' for all elements in 'squares'")
   
    def test_variable_values(self):
        self.assertTrue(isinstance(self.BODY_PARTS, int) and self.BODY_PARTS > 0, "Expected BODY_PARTS is a positive integer")
        self.assertTrue(isinstance(self.SPACE_SIZE, int) and self.SPACE_SIZE > 0, "Expected SPACE_SIZE is positive integer")

    def test_snake_color(self):
        self.assertRegex(SNAKE_COLOR, "^#[0-9A-Fa-f]{6}$", "Expected SNAKE_COLOR is a valid hex color value")

if __name__ == "__main__":
    unittest.main(verbosity=2)
