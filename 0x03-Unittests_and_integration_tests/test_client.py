#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class in client module.
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, mock_get_json.return_value)
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == "__main__":
    unittest.main()
