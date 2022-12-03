from unittest import TestCase
from game import validate_move


class ValidateMove(TestCase):
    def test_validate_move_up(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Up"
        actual = validate_move(character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_down(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Down"
        actual = validate_move(character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_left(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 5, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Left"
        actual = validate_move(character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_right(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 5, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Right"
        actual = validate_move(character, direction)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_hit_down_wall(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [4, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Down"
        actual = validate_move(character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_hit_up_wall(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Up"
        actual = validate_move(character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_hit_left_wall(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 0, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Left"
        actual = validate_move(character, direction)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_hit_right_wall(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 9, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Shuyi'}
        direction = "Right"
        actual = validate_move(character, direction)
        expected = False
        self.assertEqual(expected, actual)
