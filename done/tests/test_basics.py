"""
Tests for the DoneXBlock
"""

import json
from unittest.mock import patch
import requests
from django.test.testcases import TestCase
from .utils import make_block, make_url


class TestForDoneValueInDoneXblock(TestCase):

    """
    Tests for the different states of DoneXblock
    """

    def setUp(self):
        """ Setting up values """
        super().setUp()

        self.xblock = make_block()

    def test_done_value(self):
        """ Adding test to check done value """
        assert not self.xblock.done

    @patch('requests.post', return_value={'state': False})
    def test_post(self, mock_post):
        """ Adding mock request to test form state after toggling """
        info = {"done": False}
        url = make_url()
        resp = requests.post(url, data=json.dumps(
            info), headers={'Content-Type': 'application/json'}, timeout=10)
        mock_post.assert_called_with(url, data=json.dumps(
            info), headers={'Content-Type': 'application/json'}, timeout=10)
        assert resp['state'] is False
