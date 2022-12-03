from unittest import TestCase
from unittest.mock import patch

from game import event_option


class EventOption(TestCase):

    @patch('random.choice', return_value='Nero')
    def test_event_option_penelope(self, mock_input):
        character = {'X-coordinate': 9, 'Y-coordinate': 4, 'Nero': [5, 20], 'Lulu': [1, 10], 'Noah': [1, 10],
                     'Penelope': [1, 10], 'Name': 'Chris'}
        actual = event_option(character)
        self.assertEqual('Nero', actual)

# not working