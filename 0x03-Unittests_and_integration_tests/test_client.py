#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test that GithubOrgClient.public_repos returns the correct
        repositories.
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo: dict, license_key: str,
                         expected: bool) -> None:
        """
        Test that GithubOrgClient.has_license returns the correct
        boolean value.
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0], "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2], "apache2_repos": TEST_PAYLOAD[0][3]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test case for the GithubOrgClient class in client module.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class by patching requests.get to return example payloads.
        """
        cls.get_patcher = patch('requests.get',
                                side_effect=cls.mocked_requests_get)
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class by stopping the patcher.
        """
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """
        Mock function to return the appropriate payload based on the URL.
        """
        if url == "https://api.github.com/orgs/google":
            return MockResponse(TEST_PAYLOAD[0][0])
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(TEST_PAYLOAD[0][1])
        return MockResponse(None, 404)

    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos returns the expected
        list of repositories.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), TEST_PAYLOAD[0][2])

    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos returns the expected list
        of repositories with a specific license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         TEST_PAYLOAD[0][3])


class MockResponse:
    """
    Mock response class to simulate the requests.Response object.
    """

    def __init__(self, json_data, status_code=200):
        """
        Initialize the MockResponse object with the provided JSON data
        and status code.
        """
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """
        Return the JSON data of the response.
        """
        return self.json_data


if __name__ == "__main__":
    unittest.main()
