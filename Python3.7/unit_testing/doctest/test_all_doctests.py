import unittest
import doctest
import yatzy


def load_tests(loader, tests, ignore):
    tests.addTest(doctest.DocTestSuite(yatzy))
    return tests
