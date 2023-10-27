import unittest
import tkinter as tk
from unittest import mock
import snake_game


class TestGameOver(unittest.TestCase):
    
    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_normal_function_execution(self, mock_canvas):
        snake_game.game_over()
        mock_canvas.delete.assert_called_once_with(tk.ALL)
        mock_canvas.create_text.assert_called_once()

    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_function_execution_on_empty_canvas(self, mock_canvas):
        mock_canvas.find_all.return_value = []
        snake_game.game_over()
        mock_canvas.delete.assert_not_called()
        mock_canvas.create_text.assert_called_once()

    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_function_execution_on_non_empty_canvas(self, mock_canvas):
        mock_canvas.find_all.return_value = [1]
        snake_game.game_over()
        mock_canvas.delete.assert_called_once_with(tk.ALL)
        mock_canvas.create_text.assert_called_once()

    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_resize_during_function_execution(self, mock_canvas):
        snake_game.game_over()
        mock_canvas.create_text.assert_called_with(mock_canvas.winfo_width()/2, mock_canvas.winfo_height()/2,
                                                   font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_terminate_during_function_execution(self, mock_canvas):
        mock_canvas.create_text.side_effect = tk.TclError 
        with self.assertRaises(tk.TclError):
            snake_game.game_over()
    
    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_font_availability(self, mock_canvas):
        # TODO: This test depends on the particular system where it's being run.
        # Replace NotImplemented with the correct logic
        # Generally, this could lead to substituting default system font or failing. 
        # Validation will likely involve UI screenshot comparison or running tkinter._getints(mock_canvas['font']) 
        raise NotImplementedError("This test case needs to be implemented")

    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_repeated_function_execution(self, mock_canvas):
        for _ in range(5):
            snake_game.game_over()
        self.assertEqual(mock_canvas.delete.call_count, 5)
        self.assertEqual(mock_canvas.create_text.call_count, 5)

    @mock.patch('snake_game.canvas', new_callable=tk.Canvas)
    def test_use_after_function_execution(self, mock_canvas):
        mock_canvas.find_all.return_value = [1]
        snake_game.game_over()
        with self.assertRaises(Exception): 
            # TODO: Replace 'Exception' with actual exception that's raised when another function tries to interact with deleted game objects
            pass
            

if __name__ == '__main__':
    unittest.main(verbosity=2)
