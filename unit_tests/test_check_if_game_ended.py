from unittest import TestCase
from game import check_if_game_ended


class TestCheckIfGameEnded(TestCase):
    def test_check_if_game_ended_empty_list(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [4, 14], 'Lulu': [5, 12],
                     'Noah': [5, 11], 'Penelope': [1, 10], 'Name': 'Chris'}
        actual = check_if_game_ended(character)
        expected = []
        self.assertEqual(expected, actual)

    def test_check_if_game_ended_one_item_in_list(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [4, 14], 'Lulu': [5, 12],
                     'Noah': [2, 15], 'Penelope': [1, 10], 'Name': 'Chris'}
        actual = check_if_game_ended(character)
        expected = ['Noah']
        self.assertEqual(expected, actual)

    def test_check_if_game_ended_two_items_in_list(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [4, 14], 'Lulu': [2, 15],
                     'Noah': [2, 15], 'Penelope': [1, 10], 'Name': 'Chris'}
        actual = check_if_game_ended(character)
        expected = ['Lulu', 'Noah']
        self.assertEqual(expected, actual)

    def test_check_if_game_ended_all_items_in_list(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 4, 'Nero': [3, 14], 'Lulu': [2, 15],
                     'Noah': [2, 15], 'Penelope': [1, 10], 'Name': 'Chris'}
        actual = check_if_game_ended(character)
        expected = ['Nero', 'Lulu', 'Noah']
        self.assertEqual(expected, actual)
