import unittest
import sys
from importlib import import_module
from typing import Type, List

class LeetcodeTests(unittest.TestCase):
    solution_class = None
    testcases = []
           
    def test_all_cases(self):
        for input, expected in self.testcases:
            with self.subTest(f'Test for {input}'):
                self.assertEqual(self.solution_class.impl(input), expected)

def run_tests(solution_class, testcases):
    LeetcodeTests.solution_class = solution_class
    LeetcodeTests.testcases = testcases
    unittest.main()