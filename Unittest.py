import unittest as ut
import datalag as dl
import logiklag as ll

class Testfunctions(ut.testcase):

    def test_notspecifiedinit(self):
        testdatalag = dl.datalag()
        self.assertEqual(testdatalag.brikker, 4)
        self.assertEqual(testdatalag.muligheder, 6)
        self.assertEqual(testdatalag.maks, 10)
        self.assertTrue(isinstance(testdatalag.solution, tuple))
        self.assertEqual(len(testdatalag.solution), testdatalag.brikker)

    def test_specifiedinit(self):
        testdatalag = dl.datalag(brikker=6, muligheder=8, maks=12, solution=(4,6,1,2,3,8))
        self.assertEqual(testdatalag.brikker , 6)
        self.assertEqual(testdatalag.muligheder , 8)
        self.assertEqual(testdatalag.maks , 12)
        self.assertTrue(isinstance(testdatalag.solution, tuple))
        self.assertEqual(len(testdatalag.solution), testdatalag.brikker)
        self.assertEqual(testdatalag.solution, (4,6,1,2,3,8))

    def test_get(self):
        testdatalag = dl.datalag(brikker=6, muligheder=8, maks=12, solution=(4,6,1,2,3,7))
        self.assertEqual(testdatalag.getbrikker(), 6)
        self.assertEqual(testdatalag.getmuligheder(), 8)
        self.assertEqual(testdatalag.getmaks(), 12)
        self.assertEqual(testdatalag.getsolution(), (4,6,1,2,3,7))

    def test_set(self):
        testdatalag = dl.datalag(brikker=6, muligheder=8, maks=12, solution=(4,6,1,2,3,7))
        testdatalag.setbrikker(2)
        self.assertEqual(testdatalag.getbrikker(), 2)
        testdatalag.setmuligheder(69)
        self.assertEqual(testdatalag.getmuligheder(), 69)
        testdatalag.setmaks(42)
        self.assertEqual(testdatalag.getmaks(), 42)
        testdatalag.setsolution(4,6)
        self.assertEqual(testdatalag.getsolution(), [4,6])
        with self.assertRaises(TypeError):
            testdatalag.setbrikker("Epstein didn't kill himself")
        with self.assertRaises(TypeError):
            testdatalag.setmuligheder(4.0)
        with self.assertRaises(TypeError):
            testdatalag.setmaks("EXDEE IM PICKLE WICK JOHN WICK FORTNITE UWU JOHN FORTNITE PICKLE WICK UWU")