from unittest import TestCase
from game import replace_mc_name


class TestReplaceMcName(TestCase):
    def test_replace_mc_name_one_item(self):
        name = 'Alice'
        lines = ['Hello, /mc_name']
        expected = ['Hello, \033[92mAlice\033[00m']
        self.assertEqual(expected, replace_mc_name(name, lines))

    def test_replace_mc_name_many_items(self):
        name = 'Kitty'
        lines = ['My name is /mc_name', '/mc_name is doing test']
        expected = ['My name is \033[92mKitty\033[00m', '\033[92mKitty\033[00m is doing test']
        self.assertEqual(expected, replace_mc_name(name, lines))
