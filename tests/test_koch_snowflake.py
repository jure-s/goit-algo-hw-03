import unittest
from unittest.mock import patch, MagicMock
import turtle
from task2_koch_snowflake.koch_snowflake import draw_koch_snowflake, draw_koch_segment

class TestKochSnowflake(unittest.TestCase):

    def setUp(self):
        """Set up a mock turtle for testing."""
        self.mock_turtle = MagicMock(spec=turtle.Turtle)

    @patch("turtle.Screen", autospec=True)
    def test_draw_koch_segment(self, mock_screen):
        """Test drawing a single Koch segment."""
        length = 100
        level = 2

        # Call the function
        draw_koch_segment(self.mock_turtle, length, level)

        # Verify that the turtle commands are called
        self.assertTrue(self.mock_turtle.forward.called)
        self.assertTrue(self.mock_turtle.left.called)
        self.assertTrue(self.mock_turtle.right.called)

    @patch("turtle.Screen", autospec=True)
    def test_draw_koch_snowflake(self, mock_screen):
        """Test drawing the Koch snowflake."""
        length = 200
        level = 2

        # Call the function
        draw_koch_snowflake(self.mock_turtle, length, level)

        # Verify that the turtle commands are called
        self.assertTrue(self.mock_turtle.forward.called)
        self.assertTrue(self.mock_turtle.left.called)
        self.assertTrue(self.mock_turtle.right.called)

        # Verify the three main rotations for the snowflake (120 degrees each)
        self.assertEqual(self.mock_turtle.right.call_args_list[-3:], [((120,),), ((120,),), ((120,),)])

if __name__ == "__main__":
    unittest.main()
