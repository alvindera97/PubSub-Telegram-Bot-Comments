"""
Module for tests on [user] roles.

This module contains test cases for testing user roles and their functionality.

Classes:
  TestRolesTestCase: Provides test methods for unit tests on user roles.

Methods:
  setUp(): Prepares test environment before each individual test.
  tearDown(): Cleans up test environment after each test.
"""
import inspect
import unittest
from enum import Enum

from roles import role


class TestRolesTestCase(unittest.TestCase):
    """
    Test case class for tests for user roles.
    """

    @classmethod
    def setUpClass(cls):
        """
        Method defining executions before starting of tests in the class.

        Differs from self.setUp() as self.setUp() is called before every test
        while self.setUpClass() is called before start of all the tests in the
        class exactly once.
        :return:
        """
        super().setUpClass()
        cls.roles = role.Roles

    def setUp(self) -> None:
        """
        Method defining what must be run before each individual test.
        :return: None
        """
        super().setUp()

    def teatDown(self) -> None:
        """
        Method defining actions after each individual test.
        :return: None
        """
        super().tearDown()

    def test_roles_enum_class_exists(self) -> None:
        """
        Tests if the Roles enum class exists.
        :return: None
        """
        self.assertTrue(inspect.isclass(role.Roles))

    def test_roles_is_an_enum_instance_is_of_roles_class(self):
        """
        Tests if the roles object is of type Enum class
        :return: None
        """
        self.assertEqual(type(self.roles), type(Enum))


if __name__ == "__main__":
    unittest.main()
