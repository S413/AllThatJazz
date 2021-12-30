import sys
import os
import timeit
import unittest

from objectiveFun import ObjectiveFun

class setupTest(unittest.TestCase):
    def test_object_basic(self):
        cost = ObjectiveFun()

        cost.print_expr()

        self.assertEqual(cost.evaluate([0,0,0,0, 0, 13]), 13.0)


