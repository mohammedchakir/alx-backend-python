#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            org_payload = {"repos_url": "https://api.github.com/orgs /\
                           /test_org/repos"}
            mock_org.return_value = org_payload
            client = GithubOrgClient("test_org")
            result = client._public_repos_url
            expected_result = org_payload["repos_url"]
            self.assertEqual(result, expected_result)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the
        correct list of repos.
        """
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        mock_get_json.return_value = mock_payload

        client = GithubOrgClient("test_org")
        repos = client.public_repos

        mock_get_json.assert_called_once_with(
            'https://api.github.com/orgs/test_org/repos')
        self.assertEqual(repos, [repo['name'] for repo in mock_payload])


if __name__ == "__main__":
    unittest.main()
