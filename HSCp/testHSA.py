import sys
import os
import timeit
import unittest

from HSA import StandardHarmonySearch
import HSCp as harsea
from objectiveFun import ObjectiveFun

class HSTests(unittest.TestCase):
    def test_base(self):
        nVar = 2
        memSize = 4
        c = [(-300,500),(-300,500)]
        
        harsea1 = harsea.HarmonySearch(memSize, nVar, c)

        iterations = 100
        syms = ['x', 'y']
        expr = '(1-x)**2 + 100*(y-x**2)**2'
        HS1 = StandardHarmonySearch(harsea1, syms, expr, iterations)

        HS1.Jam()

    def test_correct(self):
        nVar = 2
        memSize = 100
        c = [(-10,10),(-10,10)]

        harsea1 = harsea.HarmonySearch(memSize, nVar, c)

        iterations = 10000
        syms = ['x', 'y']
        expr = '(1-x)**2 + 100*(y-x**2)**2'
        HS1 = StandardHarmonySearch(harsea1, syms, expr, iterations)

        HS1.Jam()

        #self.assertEqual(HS1.memory[HS1.best,0],1)
        #self.assertEqual(HS1.memory[HS1.best,1],1)

        self.assertAlmostEqual(HS1.fitness[HS1.best],0)
        #self.assertEqual(Hs1.fitness[HS1.best],0)
