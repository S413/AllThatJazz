import sys
import os
import timeit
import unittest

from objectiveFun import ObjectiveFun

class setupTest(unittest.TestCase):
    def test_object_basic(self):
        cost = ObjectiveFun(['x','y'], '(1-x)**2+100*(y-x**2)**2')

        cost.print_expr()

        self.assertEqual(cost.evaluate([1,1]), 0)


