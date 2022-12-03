import io
from unittest import TestCase
from unittest.mock import patch

from game import make_character


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=[" "])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_character(self, mock_output, mock_input):
        make_character()
        actual = mock_output.getvalue()
        expected = "Please enter a non-empty character name"
        self.assertEqual(expected, actual)

