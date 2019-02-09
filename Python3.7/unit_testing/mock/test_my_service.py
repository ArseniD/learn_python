import unittest

from unittest.mock import *
from my_service import MyService
from single_sign_on import *


class MyServiceTest(unittest.TestCase):
    def test_invalid_token(self):
        registry = FakeSingleSignOnRegistry()
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=None)
        self.assertIn("please enter your login details", response)

    def test_valid_token(self):
        registry = FakeSingleSignOnRegistry()
        token = registry.register("valid credentials")
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        self.assertIn("hello world", response)

    def test_invalid_tolen_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=False)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token=token)
        # check that mock was called during the test, is_valid was called on
        # the mock registry
        self.assertTrue(registry.is_valid_was_called)

    def test_valid_token_with_mock(self):
        token = SSOToken()
        registry = MockSingleSignOnRegistry(expected_token=token, token_is_valid=True)
        my_service = MyService(registry)

        response = my_service.handle_request("do stuff", token)
        # check that mock was called during the test, is_valid was called on
        # the mock registry
        self.assertTrue(registry.is_valid_was_called)


