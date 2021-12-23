import sys
import os
import timeit
import unittest

import HSCp as harsea

class setupTest(unittest.TestCase):
    def make_memory(self, memSize, varNum, ex):

        mem0 = harsea.HarmonyMemory(memSize, varNum)
        mem1 = harsea.HarmonyMemory(memSize, varNum)
        mem2 = harsea.HarmonyMemory(memSize+ex, varNum+ex)

        return mem0, mem1, mem2

    def make_hs(self, memSize, varNum, xDom):
        
        hs1 = harsea.HarmonySearch(memSize, varNum, xDom)

        return hs1

    def test_basic(self):

        memSize = 4
        varNum = 3
        ex = 2

        mem0, mem1, mem2, *_ = self.make_memory(memSize, varNum, ex)

        self.assertEqual(memSize, mem0.HMS)
        self.assertEqual(memSize, mem1.HMS)
        self.assertEqual(memSize+ex, mem2.HMS)

        self.assertEqual(varNum, mem0.N)
        self.assertEqual(varNum, mem1.N)
        self.assertEqual(varNum+ex, mem2.N)

        xDom = [(-2,2),(0,4),(-3,0)]
        xDomex = [(0,2),(-2,0),(-4,-1),(5,6),(1,10)]

        hs1 = self.make_hs(memSize, varNum, xDom)
        hs2 = self.make_hs(memSize+ex, varNum+ex, xDomex)

        self.assertEqual(memSize, hs1.retrieveMem().HMS)
        self.assertEqual(memSize+ex, hs2.retrieveMem().HMS)
        self.assertEqual(varNum, hs1.retrieveMem().N)
        self.assertEqual(varNum+ex, hs2.retrieveMem().N)

        for it in range(memSize):
            for jt in range(varNum):
                self.assertTrue(hs1.retrieveMem()[it,jt] >= xDom[jt][0] and hs1.retrieveMem()[it,jt] <= xDom[jt][1])

    def testSearch_constructor(self):
        memSize = 4
        varNum = 4

        memo1,_,_ = self.make_memory(memSize, varNum,0)

        for i in range(memo1.HMS):
            for j in range(memo1.N):
                memo1[i,j] = i*10+j

        hsearch1 = self.make_hs(memSize, varNum, [(0,2),(-2,0),(5,8),(-1,3)])

        print("Before Making hsearch.")

        hsearch2 = harsea.HarmonySearch(memo1, [(0,2), (-2,0), (5,8), (-1,3)])

        hsearch2.viewMemory()

        print("We are to assume we can't viewMemory().")


