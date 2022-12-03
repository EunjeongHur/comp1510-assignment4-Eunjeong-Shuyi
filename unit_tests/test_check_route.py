import io
from unittest import TestCase
from unittest.mock import patch
from game import check_route


class TestCheckRoute(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_route_true(self, mock_output):
        character = {'X-coordinate': 3, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 15], 'Name': 'Alice'}
        self.assertEqual(True, check_route(character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_route_penelope_episode_two(self, mock_output):
        character = {'X-coordinate': 3, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [2, 18], 'Name': 'Alice'}
        self.assertEqual(True, check_route(character))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_route_false(self, mock_output):
        character = {'X-coordinate': 3, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [2, 10], 'Name': 'Alice'}
        self.assertEqual(False, check_route(character))
