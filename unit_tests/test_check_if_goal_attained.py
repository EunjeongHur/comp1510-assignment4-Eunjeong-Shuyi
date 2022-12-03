from unittest import TestCase
from game import check_if_goal_attained


class Test(TestCase):
    def test_check_if_goal_attained_nero_true(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Alice'}
        self.assertEqual(True, check_if_goal_attained(character))

    def test_check_if_goal_attained_nero_false(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [4, 17], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Alice'}
        self.assertEqual(False, check_if_goal_attained(character))

    def test_check_if_goal_attained_lulu_true(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [1, 10], 'Lulu': [6, 21], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Alice'}
        self.assertEqual(True, check_if_goal_attained(character))

    def test_check_if_goal_attained_lulu_false(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [1, 10], 'Lulu': [5, 18], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Alice'}
        self.assertEqual(False, check_if_goal_attained(character))

    def test_check_if_goal_attained_noah_true(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [1, 10], 'Lulu': [1, 10], 'Noah': [6, 20],
                     'Penelope': [1, 10], 'Name': 'Alice'}
        self.assertEqual(True, check_if_goal_attained(character))

    def test_check_if_goal_attained_noah_false(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [1, 10], 'Lulu': [1, 10], 'Noah': [4, 19],
                     'Penelope': [1, 10], 'Name': 'Alice'}
        self.assertEqual(False, check_if_goal_attained(character))

    def test_check_if_goal_attained_penelope_true(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [1, 10], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [5, 22], 'Name': 'Alice'}
        self.assertEqual(True, check_if_goal_attained(character))

    def test_check_if_goal_attained_penelope_false(self):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [1, 10], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [4, 20], 'Name': 'Alice'}
        self.assertEqual(False, check_if_goal_attained(character))
