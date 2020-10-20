import unittest
from unittest import TestCase
from unittest.mock import patch
import requests

import bitcoin

class TestBitCoin(TestCase):



    @patch('builtins.input', side_effect=['2'])
    def test_user_input(self, mock_input):
        bit = bitcoin.get_user_input()
        self.assertEqual(2.0, bit)

    ### I understand the mocking for user input and test data but im still 
    ### a little fuzzy on testing api calls with no params , i'm going to leave it hear for noe
    ### so i can work with my group on the project but i will keep looking into api test calls



if __name__ == '__main__':
    unittest.main()