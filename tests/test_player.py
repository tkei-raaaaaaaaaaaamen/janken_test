import unittest
from unittest.mock import patch
from source.player import player_pon

# テストクラス
class TestPlayerModule(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_guu(self, mock_input):
        self.assertEqual(player_pon(), 'グー')
        
    @patch('builtins.input', return_value='2')
    def test_tyoki(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')
        
    @patch('builtins.input', return_value='3')
    def test_paa(self, mock_input):
        self.assertEqual(player_pon(), 'パー')

if __name__ == '__main__':
    unittest.main()
