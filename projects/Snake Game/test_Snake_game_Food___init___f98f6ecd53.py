'''
1. Validate that the generated x-coordinate is within the expected range (0 to (GAME_WIDTH / SPACE_SIZE) - 1) multiplied by SPACE_SIZE.
2. Validate that the generated y-coordinate is within the expected range (0 to (GAME_HEIGHT / SPACE_SIZE) - 1) multiplied by SPACE_SIZE.
3. Verify that the coordinates attribute of the object gets assigned correctly with [x, y] after the function.
4. Check that the function correctly creates an oval on the canvas at the coordinates (x, y).
5. Ensure that the overall size of the oval created on the canvas is correct, i.e., (x + SPACE_SIZE, y + SPACE_SIZE).
6. Check if the oval color is set to be FOOD_COLOR.
7. Verify that the created oval is correctly tagged as "food".
8. Test with different values of GAME_WIDTH, GAME_HEIGHT, SPACE_SIZE and verify the function behaves as expected.
9. Run multiple iterations of the scenario to account for the randomness of the x and y value generation and ensure they are consistently within expected boundaries.
10. Check the function's behavior if an attempt is made to create an oval at coordinates already occupied by a pre-existing element.
11. Test for possible exceptions or error scenarios when values of the coordinates x and y exceed the canvas limits or when the space size exceeds the game dimensions. 
'''
import unittest
from unittest.mock import patch, MagicMock
from tkinter import Canvas
from snake_game import Food

class TestFoodInit(unittest.TestCase):
    GAME_WIDTH = 700
    GAME_HEIGHT = 700
    SPACE_SIZE = 50
    FOOD_COLOR = '#FF0000'

    def setUp(self):
        self.canvas_mock = MagicMock(spec=Canvas)

    @patch('snake_game.random.randint')
    def test_init(self, random_mock):
        for i in range(100):  # Run multiple iterations to account for randomness
            x_coordinate = i * self.SPACE_SIZE
            y_coordinate = i * self.SPACE_SIZE
            # Place the object initialisation with required parameters inside the loop
            self.food = Food(self.canvas_mock, self.GAME_WIDTH, self.GAME_HEIGHT, self.SPACE_SIZE, self.FOOD_COLOR)

            # Set the return value of random.randint to our determined x and y coordinates
            random_mock.side_effect = [x_coordinate, y_coordinate]

            # Verify x, y coordinates are correct
            self.assertEqual(self.food.coordinates, [x_coordinate, y_coordinate])

            # Check that create_oval is called with the correct arguments
            self.canvas_mock.create_oval.assert_called_with(
                x_coordinate, 
                y_coordinate, 
                x_coordinate + self.SPACE_SIZE, 
                y_coordinate + self.SPACE_SIZE, 
                fill=self.FOOD_COLOR, 
                tag="food"
            )

            # Clear the mock for the next iteration
            self.canvas_mock.reset_mock()

    # TODO: Create more test methods to test exceeding canvas limits, game dimensions, 
    # and behavior with pre-existing elements at the coordinates

if __name__ == "__main__":
    unittest.main(verbosity=2)
