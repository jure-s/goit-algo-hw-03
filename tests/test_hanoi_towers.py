import unittest
from unittest.mock import patch, MagicMock
from task3_hanoi_towers.hanoi_towers import hanoi_towers

class TestHanoiTowers(unittest.TestCase):

    def setUp(self):
        """Set up the initial state for testing."""
        self.state = {
            'A': [3, 2, 1],  # Three disks on rod A
            'B': [],          # Rod B is empty
            'C': []           # Rod C is empty
        }
        self.rod_positions = {'A': -200, 'B': 0, 'C': 200}  # Mocked rod positions

    def test_hanoi_towers_three_disks(self):
        """Test the Tower of Hanoi solution with three disks."""
        expected_final_state = {
            'A': [],           # Rod A should be empty
            'B': [],           # Rod B should be empty
            'C': [3, 2, 1]     # All disks should be on rod C
        }

        # Mock the update_visualization function to prevent graphical execution
        with patch("task3_hanoi_towers.hanoi_towers.update_visualization", return_value=None):
            hanoi_towers(3, 'A', 'C', 'B', self.state, self.rod_positions)

        self.assertEqual(self.state, expected_final_state)

    def test_hanoi_towers_one_disk(self):
        """Test the Tower of Hanoi solution with one disk."""
        self.state = {
            'A': [1],  # One disk on rod A
            'B': [],   # Rod B is empty
            'C': []    # Rod C is empty
        }

        expected_final_state = {
            'A': [],    # Rod A should be empty
            'B': [],    # Rod B should be empty
            'C': [1]    # Disk should be on rod C
        }

        with patch("task3_hanoi_towers.hanoi_towers.update_visualization", return_value=None):
            hanoi_towers(1, 'A', 'C', 'B', self.state, self.rod_positions)

        self.assertEqual(self.state, expected_final_state)

if __name__ == "__main__":
    unittest.main()