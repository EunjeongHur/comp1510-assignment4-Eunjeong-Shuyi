from unittest import TestCase
from unittest.mock import patch

from game import event_option


class TestEventOption(TestCase):

    @patch('random.choice', return_value='Nero')
    def test_event_option_nero(self, random_value):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Chris'}
        actual = event_option(character)
        self.assertEqual('Nero', actual)

    @patch('random.choice', return_value='Lulu')
    def test_event_option_lulu(self, random_value):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Chris'}
        actual = event_option(character)
        self.assertEqual('Lulu', actual)

    @patch('random.choice', return_value='Noah')
    def test_event_option_noah(self, random_value):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Chris'}
        actual = event_option(character)
        self.assertEqual('Noah', actual)

    @patch('random.choice', return_value='Penelope')
    def test_event_option_penelope(self, random_value):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Chris'}
        actual = event_option(character)
        self.assertEqual('Penelope', actual)
